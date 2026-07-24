# BabyView Objects — manuscript analyses (2026)

Analysis code for the *BabyView Objects* manuscript.

**Start here:** [`../../README.md`](../../README.md) (Nature checklist-style
install/demo), [`../../REPRODUCING.md`](../../REPRODUCING.md), and
[`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md). Pipeline detail and figure ↔
file mapping: [`REPRODUCTION.md`](REPRODUCTION.md).

## Quick links

| Resource | Purpose |
|----------|---------|
| [`../../README.md`](../../README.md) | System requirements, install, demo, licenses |
| [`../../REPRODUCING.md`](../../REPRODUCING.md) | Capsule run and scope |
| [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md) | Data/code availability + manuscript paste text |
| https://doi.org/10.24433/CO.0860553.v1 | Code Ocean capsule (provisional DOI) |
| [REPRODUCTION.md](REPRODUCTION.md) | Notebook order, dependencies, outputs |
| [SCRIPTS.md](SCRIPTS.md) | Helper scripts in [`scripts/`](scripts/) |
| [`../../data/shared_data_manuscript_2026/`](../../data/shared_data_manuscript_2026/) | Anonymized result tables |
| [requirements-manuscript.txt](requirements-manuscript.txt) | Python packages |
| [manuscript_config.py](manuscript_config.py) | Path helpers |

```bash
# from capsule root
./code/run
```

Run notebooks with working directory `code/manuscript-2026/`.

## Analyses

Category embedding tables for notebooks **02–05** are shipped under
`exemplar_set_embeddings/` (Stage 0 GPU builders are not part of this capsule).

| # | Notebook | Summary | In default `code/run`? |
|---|----------|---------|------------------------|
| 01 | `01_long_tailed_distribution.ipynb` | Detection frequencies & power-law | No — verify anonymized CSV |
| 02 | `02_category-wise_cosine_sim.ipynb` | BV vs THINGS category cosine | Optional (`RUN_NOTEBOOKS=1`) |
| 03 | `03_bv_things_rdm_comparison.ipynb` | RDM comparison & figures | Optional (`RUN_NOTEBOOKS=1`) |
| 04 | `04_individual_rdms.ipynb` | Per-child RDMs | No — verify anonymized CSV |
| 05 | `05_within_between_cdi_cluster_correlation.ipynb` | CDI cluster geometry | Optional (`RUN_NOTEBOOKS=1`) |
| 06–07 | *(Stage 0; not shipped)* | Build category embeddings | No — tables already included |
| 08 | `08_animal_depiction_label_proportions.ipynb` | Animal depiction supplement | No — verify anonymized CSV |

Scripts included in the default run: none beyond verification and copying of
anonymized tables. Optional: `RUN_NOTEBOOKS=1` for **02 / 03 / 05**. See
[SCRIPTS.md](SCRIPTS.md).

## Key paths

| Path | Role |
|------|------|
| `exemplar_set_embeddings/` | Category-level z-scored tables |
| `../../data/shared_data_manuscript_2026/` | Anonymized aggregates |
| `../../results/` | Written by `code/run` |

## Conventions

- `CATEGORY_SET`: `valid129` (main text) or `valid85` (supplement).
- `PREPRINT_DIR` is an alias for this folder (`manuscript_config.PREPRINT_DIR`).
