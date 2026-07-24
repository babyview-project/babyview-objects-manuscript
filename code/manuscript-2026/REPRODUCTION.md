# Reproducing BabyView Objects (manuscript 2026)

How to verify or rerun analyses reported in *BabyView Objects* (June 2026).

For the capsule Reproducible Run, start with
[`../../REPRODUCING.md`](../../REPRODUCING.md) and
[`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md). This file maps notebooks to
outputs and notes which steps need restricted BabyView data.

Anonymized tables:
[`data/shared_data_manuscript_2026/`](../../data/shared_data_manuscript_2026/).

## Layout (this capsule)

```text
code/manuscript-2026/
├── scripts/                                      # helpers (stats, capsule reproduce)
├── 01_long_tailed_distribution.ipynb             # needs frame detections (Tier D)
├── 02_category-wise_cosine_sim.ipynb             # Tier B embeddings
├── 03_bv_things_rdm_comparison.ipynb             # Tier B
├── 04_individual_rdms.ipynb                      # Tier C per-image .npy
├── 05_within_between_cdi_cluster_correlation.ipynb  # Tier B
├── 08_animal_depiction_label_proportions.ipynb      # annotation / Tier A verify
├── exemplar_set_embeddings/{valid129,valid85}/   # shipped Tier B tables
├── manuscript_config.py
├── requirements-manuscript.txt
├── SCRIPTS.md
└── DATA_AVAILABILITY.md

code/run                                          # Code Ocean entry point
data/shared_data_manuscript_2026/                 # Tier A (MANIFEST.json)
```

Stage 0 notebooks **06–07** and GPU builders are not included here;
this capsule ships precomputed `exemplar_set_embeddings/` instead.

## Environment

```bash
pip install -r code/manuscript-2026/requirements-manuscript.txt
# notebooks: cwd = code/manuscript-2026/
```

## Data tiers

| Tier | What | Who needs it |
|------|------|----------------|
| **A — `data/shared_data_manuscript_2026/`** | Result CSVs, category lists, embedding copies | Anyone verifying paper numbers |
| **B — `exemplar_set_embeddings/`** | Category z-score tables (shipped in capsule) | Regenerating **02**, **03**, **05** + scripts |
| **C — Per-image `.npy`** | Crop embeddings under `BV_EMBEDDINGS_BASE` | **04**, Stage 0 rebuild |
| **D — Raw detections / video** | YOLOE / BabyView access | **01** from scratch; **08** from annotation |

## Recommended workflow

### Default capsule run (verify + regenerate from shipped embeddings)

```bash
./code/run
```

See [`REPRODUCING.md`](../../REPRODUCING.md).

### Verify manuscript statistics (Tier A only)

Compare `data/shared_data_manuscript_2026/results_valid129/` to the manuscript.
No recompute required.

### Regenerate from shipped embeddings (Tier B)

| Step | Notebook / script | Capsule notes |
|------|-------------------|---------------|
| 2 | **02** | Optional: `RUN_NOTEBOOKS=1` |
| 3 | **03** | Optional: `RUN_NOTEBOOKS=1` |
| 4 | **05** | Optional: `RUN_NOTEBOOKS=1` |

### Restricted data (Tier C / D) — requires BabyView access

These steps are documented for completeness. They are **not** part of the
default capsule run; corresponding headline statistics are provided as
anonymized CSVs under `data/shared_data_manuscript_2026/`.

| Step | Notebook / script | Produces |
|------|-------------------|----------|
| 0 | Stage 0 (**06→07**) | `exemplar_set_embeddings/` (CLIP / DINOv3) |
| 1 | **01** | Long-tail CSVs |
| 7 | **04** | Individual & top-8 RDM panels |
| 8 | **08** | Animal depiction proportions |

Set `CATEGORY_SET` to `valid129` (main) or `valid85` (supplement). Filenames use
threshold token `filtered-0.27`.

## Figure ↔ artifact mapping (valid129 main text)

| Manuscript topic | Primary outputs | Notebook / script |
|------------------|-----------------|-------------------|
| Long-tailed category frequencies | `long_tailed_*_valid129.csv` | **01** (Tier A CSV shipped) |
| BV–THINGS category cosine | `category_wise_cosine_similarity_*_valid129.csv` | **02** |
| RDM structure (CLIP / DINOv3) | `bv_things_rdm_comparison_*` | **03** |
| CDI cluster within/between | `cluster_within_between_*`, `bv_vs_things_cluster_strength_*` | **05** |
| Top-8 RDM agreement | `individual_rdm_pairwise_*_top8_densest_*` | **04** (Tier A CSV shipped) |
| Animal depiction supplement | `animal_depiction_label_proportions_by_category.csv` | **08** (also in Tier A `inputs/`) |

Supplement (valid85): `02`–`03` with `CATEGORY_SET=valid85`.

## Category sets

- **valid129** — 129 CDI categories (precision ≥ 0.6, CLIP filter 0.27).
- **valid85** — Supplement / top-8 subset.

## Privacy

- Released tables use pseudonyms `participant_01`–`participant_08` (densest-first);
  see `data/shared_data_manuscript_2026/metadata/participant_registry_top8.csv`.
- This capsule does not include raw annotation filenames, video paths, or
  real family identifiers.

## Data and code availability

See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) (includes GitHub link, Code
Ocean DOI https://doi.org/10.24433/CO.0860553.v1, licenses, and suggested
manuscript availability text).
