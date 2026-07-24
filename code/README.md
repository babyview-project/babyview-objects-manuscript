# BabyView Objects — analysis code

Manuscript analysis code and category-level embedding tables for *BabyView
Objects* (2026).

## Layout

```text
code/
  run                                 # Reproducible Run entry point
  manuscript-2026/                    # notebooks 01–05, 08 + scripts
  manuscript-2026/exemplar_set_embeddings/   # category embedding tables
```

Data siblings (capsule root): `data/shared_data_manuscript_2026/`, `results/`.

## Quick start

1. Click **Reproducible Run** (executes [`run`](run)).
2. Inspect `/results` (`shared/` + `regenerated_valid129/`).
3. Optionally compare manuscript numbers to CSVs in
   `../data/shared_data_manuscript_2026/results_valid129/`.

Details: [`../REPRODUCING.md`](../REPRODUCING.md) ·
availability: [`manuscript-2026/DATA_AVAILABILITY.md`](manuscript-2026/DATA_AVAILABILITY.md).

From a local checkout of this capsule:

```bash
./code/run
```

## Scope of the default run

Included: verification of anonymized tables; regeneration of analyses that use
only shipped category embeddings (see `REPRODUCING.md`).

Not included in the default run (restricted BabyView assets):

- Stage 0 GPU embedding builders (notebooks **06–07**)
- Notebooks **01**, **04**, **08** (headline numbers still in anonymized CSVs)
- Raw video / detection dumps / real subject IDs

## Data use

Only anonymized tables under `data/shared_data_manuscript_2026/` are intended for
redistribution with this capsule. Per-image embeddings and raw video require
BabyView data-use agreements.
