"""Shared paths for manuscript-2026 (BabyView Objects manuscript).

Works in both layouts:
  - Code Ocean capsule: ``code/manuscript-2026/`` with siblings ``../data``, ``../results``
  - Internal monorepo: ``analysis/manuscript-2026/``
"""
from __future__ import annotations

from pathlib import Path

# This file lives at {code|analysis}/manuscript-2026/manuscript_config.py
MANUSCRIPT_DIR = Path(__file__).resolve().parent
# Capsule/repo root: parent of code/ or analysis/ (on Code Ocean, filesystem root
# so that DATA_DIR resolves to /data).
PROJECT_ROOT = MANUSCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
ANNOTATION_DIR = PROJECT_ROOT / "annotation"
EXEMPLAR_EMBED_ROOT = MANUSCRIPT_DIR / "exemplar_set_embeddings"
SHARED_DATA_DIR = DATA_DIR / "shared_data_manuscript_2026"

# Back-compat alias used in older notebooks/scripts
PREPRINT_DIR = MANUSCRIPT_DIR

CATEGORY_SET_FILES: dict[str, Path] = {
    "valid85": DATA_DIR / "included_categories_valid85.txt",
    "valid129": DATA_DIR / "included_categories_valid129.txt",
}

# Tables expected by notebooks 02–05 (main text: valid129 + CLIP / DINOv3).
REQUIRED_EMBEDDING_MODELS: tuple[str, ...] = ("clip", "dinov3")


def resolve_manuscript_dir(cwd: Path | None = None) -> Path:
    """Find manuscript-2026 from repo root or when cwd is the analysis folder."""
    base = cwd or Path.cwd()
    candidates = [
        base,
        base / "code" / "manuscript-2026",
        base / "analysis" / "manuscript-2026",
        base.parent / "manuscript-2026",
    ]
    for c in candidates:
        if (c / "01_long_tailed_distribution.ipynb").exists():
            return c.resolve()
    return MANUSCRIPT_DIR


def resolve_code_or_analysis_dir(project_root: Path | None = None) -> Path:
    """Return the ``code/`` or ``analysis/`` directory that contains manuscript-2026."""
    root = project_root or PROJECT_ROOT
    for name in ("code", "analysis"):
        cand = root / name / "manuscript-2026"
        if cand.is_dir():
            return (root / name).resolve()
    parent = MANUSCRIPT_DIR.parent
    if parent.name in {"code", "analysis"}:
        return parent.resolve()
    return (root / "code").resolve()


def exemplar_embed_dir(category_set: str) -> Path:
    if category_set not in CATEGORY_SET_FILES:
        raise ValueError(f"Unknown category_set: {category_set!r}")
    return EXEMPLAR_EMBED_ROOT / category_set


def bv_embedding_csv(model: str, category_set: str, *, zscore: bool = True) -> Path:
    suffix = "zscore" if zscore else "raw"
    return exemplar_embed_dir(category_set) / (
        f"bv_{model}_exemplar_avg_{suffix}_within_{category_set}.csv"
    )


def things_embedding_csv(model: str, category_set: str, *, zscore: bool = True) -> Path:
    suffix = "zscore" if zscore else "raw"
    return exemplar_embed_dir(category_set) / (
        f"things_{model}_exemplar_avg_{suffix}_within_{category_set}.csv"
    )


def required_embedding_tables(
    category_set: str,
    models: tuple[str, ...] = REQUIRED_EMBEDDING_MODELS,
) -> list[Path]:
    """BV + THINGS z-scored category tables used downstream (notebooks 02–05)."""
    paths: list[Path] = []
    for model in models:
        paths.append(bv_embedding_csv(model, category_set))
        paths.append(things_embedding_csv(model, category_set))
    return paths


def missing_embedding_tables(
    category_set: str,
    models: tuple[str, ...] = REQUIRED_EMBEDDING_MODELS,
) -> list[Path]:
    return [p for p in required_embedding_tables(category_set, models) if not p.is_file()]


def cdi_semantic_csv(category_set: str, *, threshold: str = "0.27") -> Path:
    """Resolve CDI semantic map CSV (data/ root or shared_data inputs/)."""
    threshold_token = f"{float(threshold):.2f}"
    candidates = [
        DATA_DIR / f"long_tailed_dist_prop_included_categories_{category_set}.csv",
        DATA_DIR
        / f"long_tailed_dist_prop_included_categories_filtered-{threshold_token}_{category_set}.csv",
        SHARED_DATA_DIR
        / "inputs"
        / f"long_tailed_dist_prop_included_categories_{category_set}.csv",
        SHARED_DATA_DIR
        / "inputs"
        / f"long_tailed_dist_prop_included_categories_filtered-{threshold_token}_{category_set}.csv",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return candidates[0]


def main_results_root(category_set: str) -> Path:
    if category_set == "valid85":
        return MANUSCRIPT_DIR / "supplemental_results_valid85cats_04302026"
    return MANUSCRIPT_DIR / "main_results_valid129s_04302026"
