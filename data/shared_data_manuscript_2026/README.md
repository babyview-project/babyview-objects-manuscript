# Shared anonymized data (BabyView Objects)

**Demo / verification dataset** for the *BabyView Objects* manuscript (June 2026):
anonymized intermediate tables shipped with the code capsule (~11 MB).
No raw video, crop paths, or real participant identifiers.

Compare these CSVs to the manuscript, or run `code/run`
(see [`../../README.md`](../../README.md) and [`../../REPRODUCING.md`](../../REPRODUCING.md)).

Licensed under [CC0 1.0](../LICENSE).

## Layout

| Path | Contents |
|------|----------|
| `MANIFEST.json` | File list and generation timestamp |
| `metadata/participant_registry_top8.csv` | Pseudonymous top-8 ranks and valid85 coverage |
| `category_lists/` | `included_categories_valid{129,85}.txt` |
| `inputs/` | Detection prevalence, precision, animal-depiction proportions |
| `embeddings/` | Category-level z-scored exemplar means (BV + THINGS) |
| `results_valid129/` | Main-text statistics tables |
| `vqa_detections/` | YOLOE↔VQA SI summaries + figures |

## Related code

- Manuscript analyses: [`../../code/manuscript-2026/`](../../code/manuscript-2026/)
- Reproducible Run: [`../../code/run`](../../code/run)
