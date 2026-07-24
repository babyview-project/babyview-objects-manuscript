# Python scripts in `manuscript-2026/scripts/` (this capsule)

Numbered notebooks (**01–05**, **08**) are the manuscript analyses. Helper
`.py` files live under [`scripts/`](scripts/).

Run from `code/manuscript-2026/` (e.g. `python scripts/verify_shared_data.py`).
Shared paths: [`manuscript_config.py`](manuscript_config.py).

> **Note:** Stage 0 GPU builders are not included in this capsule.
> Precomputed `exemplar_set_embeddings/` tables (CLIP / DINOv3) are shipped instead.

## Present in this capsule

| Script | Role | Used by |
|--------|------|---------|
| [`manuscript_config.py`](manuscript_config.py) | Paths (`MANUSCRIPT_DIR`, `DATA_DIR`, `cdi_semantic_csv`, …) | Notebooks + scripts |
| [`scripts/_bootstrap.py`](scripts/_bootstrap.py) | `sys.path` + path aliases for CLIs | Other scripts |
| [`scripts/bv_things_cdi_shuffle_inference.py`](scripts/bv_things_cdi_shuffle_inference.py) | CDI shuffle / cluster stats (library) | Notebook **05** |
| [`scripts/verify_shared_data.py`](scripts/verify_shared_data.py) | Assert anonymized `MANIFEST.json` files exist | `code/run` |
| [`scripts/reproduce_capsule.py`](scripts/reproduce_capsule.py) | Orchestrate regenerate + copy to `/results` | `code/run` |
| [`scripts/clip_threshold_sensitivity.py`](scripts/clip_threshold_sensitivity.py) | CLIP threshold SI | Needs Tier C (not in default run) |
| [`scripts/frame_prevalence.py`](scripts/frame_prevalence.py) | Library for long-tail / VQA helpers | Notebook **01** (restricted) |
| [`scripts/run_long_tail_frame_prevalence.py`](scripts/run_long_tail_frame_prevalence.py) | Headless notebook **01** | Needs Tier D (not in default run) |

Capsule entry point: [`../run`](../run) (see [`../../REPRODUCING.md`](../../REPRODUCING.md)).

## Typical capsule commands

```bash
# from capsule root
./code/run

# or stepwise
python code/manuscript-2026/scripts/verify_shared_data.py --strict
CATEGORY_SET=valid129 python code/manuscript-2026/scripts/reproduce_capsule.py
```

## Why keep scripts separate from notebooks?

| Reason | Example |
|--------|---------|
| **Headless / CI** | `reproduce_capsule.py`, `verify_shared_data.py` |
| **Reusable library** | `bv_things_cdi_shuffle_inference.py` |
