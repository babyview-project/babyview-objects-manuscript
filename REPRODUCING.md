# Reproducing this capsule

This capsule supports computational reproducibility of *BabyView Objects*
(manuscript 2026) from anonymized intermediates. Manuscript embedding analyses
use **CLIP** and **DINOv3**. The capsule does **not** re-run pipelines that
require restricted BabyView video or per-crop embeddings.

| Resource | Link |
|----------|------|
| GitHub | https://github.com/babyview-project/babyview-objects-manuscript |
| Code Ocean (provisional DOI) | https://doi.org/10.24433/CO.0860553.v1 |
| Nature-style README (install / demo / licenses) | [`README.md`](README.md) |

## Layout

```text
code/
  run                          # Reproducible Run entry point
  manuscript-2026/             # notebooks 01–05, 08 + scripts
  manuscript-2026/exemplar_set_embeddings/   # category embedding tables
data/
  shared_data_manuscript_2026/ # anonymized result tables (MANIFEST.json)
results/                       # written by code/run
environment/
  Dockerfile
  requirements.txt
```

On Code Ocean these map to `/code`, `/data`, `/results`, and `/environment`.

## How to use this capsule

| Goal | How |
|------|-----|
| Check manuscript numbers | Open CSVs under `data/shared_data_manuscript_2026/results_valid129/` |
| Run the automated pipeline | Click **Reproducible Run** (`code/run`), then inspect `/results` |
| Recompute embedding-level analyses | Optional: `RUN_NOTEBOOKS=1` runs notebooks **02**, **03**, **05** from shipped embeddings |
| Rebuild from crops / raw video | Requires BabyView data access (not included here) |

## What `code/run` does

1. Installs Python dependencies listed in `manuscript-2026/requirements-manuscript.txt`
2. Verifies every file listed in `data/shared_data_manuscript_2026/MANIFEST.json`
3. Copies the full anonymized shared tree into `/results/shared/` (required for
   the Code Ocean computation snapshot: main-text CSVs, inputs, embeddings,
   metadata, category lists, and VQA SI summaries)

**Typical timing on a normal desktop:** dependency install ≈1 minute; default
demo (verify + copy) under 1 minute after install. See [`README.md`](README.md).

### Optional environment variables

| Variable | Default | Effect |
|----------|---------|--------|
| `CATEGORY_SET` | `valid129` | Main-text (`valid129`) or supplement (`valid85`) category set |
| `RUN_NOTEBOOKS` | `0` | `1` = also execute notebooks **02**, **03**, **05** |
| `PIP_INSTALL` | `1` | `0` = skip pip install at run time |

## Analyses outside the default run

| Notebook / stage | Reason |
|------------------|--------|
| **01** long-tailed distribution | Needs frame-level detection dump |
| **04** individual RDMs | Needs per-image `.npy` embeddings |
| **08** animal depiction | Needs annotation crops (proportions CSV shipped) |
| Stage 0 (**06–07**) | GPU re-embedding from crops |

Headline statistics from those analyses are still available as anonymized CSVs
in `data/shared_data_manuscript_2026/`.

Further detail: [`code/manuscript-2026/REPRODUCTION.md`](code/manuscript-2026/REPRODUCTION.md)
and [`code/manuscript-2026/DATA_AVAILABILITY.md`](code/manuscript-2026/DATA_AVAILABILITY.md).
