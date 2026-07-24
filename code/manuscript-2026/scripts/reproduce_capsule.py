#!/usr/bin/env python3
"""Publish capsule results for Code Ocean reproducible runs.

Default: copy anonymized shared tables into ``results/``.
Optional: execute notebooks 02 / 03 / 05 from shipped CLIP / DINOv3 embeddings.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

from _bootstrap import MANUSCRIPT_DIR, PROJECT_ROOT, SCRIPTS_DIR
from manuscript_config import RESULTS_DIR, missing_embedding_tables


def run(cmd: list[str], *, env: dict[str, str] | None = None) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True, cwd=str(MANUSCRIPT_DIR), env=env)


def copy_tree(src: Path, dst: Path) -> int:
    if not src.exists():
        return 0
    count = 0
    dst.mkdir(parents=True, exist_ok=True)
    if src.is_file():
        shutil.copy2(src, dst / src.name)
        return 1
    for path in src.rglob("*"):
        if path.is_file():
            rel = path.relative_to(src)
            out = dst / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, out)
            count += 1
    return count


def publish_shared_to_results() -> None:
    """Copy every anonymized shared file into ``/results`` for the CO snapshot.

    Code Ocean only retains files under ``/results`` in the computation
    timeline snapshot, so the full ``shared_data_manuscript_2026`` tree
    (results, inputs, embeddings, metadata, category lists, VQA SI) is
    published here — not left only under ``/data``.
    """
    shared = PROJECT_ROOT / "data" / "shared_data_manuscript_2026"
    if not shared.is_dir():
        raise FileNotFoundError(f"Missing shared data directory: {shared}")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    n = copy_tree(shared, RESULTS_DIR / "shared")
    print(f"Published {n} shared anonymized files → {RESULTS_DIR / 'shared'}")


def publish_regenerated(category_set: str) -> None:
    if category_set == "valid85":
        run_root = MANUSCRIPT_DIR / "supplemental_results_valid85cats_04302026"
        out_name = "regenerated_valid85"
    else:
        run_root = MANUSCRIPT_DIR / "main_results_valid129s_04302026"
        out_name = "regenerated_valid129"
    n = 0
    n += copy_tree(run_root / "results", RESULTS_DIR / out_name / "results")
    n += copy_tree(run_root / "figures", RESULTS_DIR / out_name / "figures")
    print(f"Published {n} regenerated files → {RESULTS_DIR / out_name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--category-set",
        default=os.environ.get("CATEGORY_SET", "valid129"),
        choices=("valid129", "valid85"),
    )
    parser.add_argument(
        "--run-notebooks",
        action="store_true",
        help="Execute notebooks 02, 03, 05 via nbconvert (requires shipped embeddings).",
    )
    args = parser.parse_args()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    publish_shared_to_results()

    if not args.run_notebooks:
        (RESULTS_DIR / "run_summary.txt").write_text(
            "Mode: verify MANIFEST + copy anonymized tables to results/.\n"
            f"Category set: {args.category_set}\n"
            "Models: CLIP, DINOv3\n"
            "Notebooks executed: False\n"
        )
        print(f"Done. Results under: {RESULTS_DIR}")
        return 0

    missing = missing_embedding_tables(args.category_set)
    if missing:
        print("ERROR: missing embedding tables required to run notebooks:", file=sys.stderr)
        for p in missing:
            print(f"  - {p}", file=sys.stderr)
        return 1

    env = {**os.environ, "CATEGORY_SET": args.category_set}
    notebooks = [
        "02_category-wise_cosine_sim.ipynb",
        "03_bv_things_rdm_comparison.ipynb",
        "05_within_between_cdi_cluster_correlation.ipynb",
    ]
    for nb in notebooks:
        run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--inplace",
                nb,
            ],
            env=env,
        )

    publish_regenerated(args.category_set)
    (RESULTS_DIR / "run_summary.txt").write_text(
        "Mode: copy anonymized tables + execute notebooks 02/03/05.\n"
        f"Category set: {args.category_set}\n"
        "Models: CLIP, DINOv3\n"
        "Notebooks executed: True\n"
    )
    print(f"Done. Results under: {RESULTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
