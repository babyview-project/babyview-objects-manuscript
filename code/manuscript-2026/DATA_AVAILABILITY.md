# Data and code availability

Analysis code, anonymized intermediate tables, and a reproducible compute
environment for *BabyView Objects* (manuscript 2026) are provided in this
repository and the accompanying Code Ocean capsule. The reproducible entry point
is `code/run` (see [`REPRODUCING.md`](../../REPRODUCING.md)). Embedding analyses
in the manuscript use **CLIP** and **DINOv3**.

| Resource | Link / location |
|----------|-----------------|
| GitHub repository | https://github.com/babyview-project/babyview-objects-manuscript |
| Code Ocean capsule (provisional DOI) | https://doi.org/10.24433/CO.0860553.v1 |
| Code license | MIT ([`code/LICENSE`](../LICENSE)) |
| Anonymized data license | CC0 1.0 ([`data/LICENSE`](../../data/LICENSE)) |
| Restricted video (BabyView 2025.1) | https://www.databrary.org/volume/1882 |

**What a Reproducible Run does.** It verifies every anonymized table listed in
`data/shared_data_manuscript_2026/MANIFEST.json` and copies that full shared tree
to `/results/shared/` (Code Ocean’s computation snapshot only retains `/results`).
Manuscript notebooks and scripts are under `code/manuscript-2026/`. Optional
notebook re-execution (`RUN_NOTEBOOKS=1`) regenerates embedding-level analyses
**02**, **03**, and **05** and also writes those outputs under `/results`.

**Anonymized intermediates (demo dataset).** Category-level embeddings,
detection-prevalence summaries, main-text result CSVs, and top-8 participant
tables (`participant_01`–`participant_08`) are in
`data/shared_data_manuscript_2026/` (see `MANIFEST.json`). No raw video, crop
paths, or real family identifiers are included. Manuscript numbers from those
analyses can be checked directly against these tables.

**Restricted data.** Per-image crop embeddings, frame-level detection dumps, and
raw egocentric video require BabyView data access under the project’s data-use
agreement. Notebooks that need those assets (**01**, **04**, **08**; Stage 0
embedding builders **06–07**) are documented in [`REPRODUCTION.md`](REPRODUCTION.md)
but are outside the default capsule run.

**Where the code’s functionality is described.** Pipeline and analysis steps
(detection → CLIP filtering → embedding → category centroids → RDMs and
permutation tests) are described in the manuscript **Methods & Materials**
section. Notebook order and figure ↔ file mapping are in
[`REPRODUCTION.md`](REPRODUCTION.md).

---

## Suggested manuscript text (Data and code availability)

Paste into the manuscript (typically after Acknowledgments or as a dedicated
statement). Update wording only if journal style requires it.

> **Data and code availability.** Analysis code for this study is available under
> the MIT license at
> https://github.com/babyview-project/babyview-objects-manuscript.
> A computational reproducibility capsule, including anonymized intermediate
> tables sufficient to verify the reported statistics and a fixed software
> environment, is archived on Code Ocean
> (https://doi.org/10.24433/CO.0860553.v1). The capsule’s default reproducible
> run verifies the shipped tables and writes them to `/results`; optional
> notebook re-execution regenerates embedding-level analyses from included
> category-level embeddings. Raw BabyView egocentric video and per-image crop
> assets are available via Databrary
> (https://www.databrary.org/volume/1882) subject to the project’s data-use
> agreement and are not redistributed with the capsule. Detailed descriptions of
> the detection, filtering, embedding, and representational-similarity pipelines
> are provided in the Methods & Materials section.
