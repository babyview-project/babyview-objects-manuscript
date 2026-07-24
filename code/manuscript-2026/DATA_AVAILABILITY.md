# Data and code availability

Analysis code, anonymized intermediate tables, and a reproducible compute
environment for *BabyView Objects* (manuscript 2026) are provided in this Code
Ocean capsule. The reproducible entry point is `code/run` (see
[`REPRODUCING.md`](../../REPRODUCING.md)). Embedding analyses in the manuscript
use **CLIP** and **DINOv3**.

**What a Reproducible Run does.** It verifies every anonymized table listed in
`data/shared_data_manuscript_2026/MANIFEST.json` and copies that full shared tree
to `/results/shared/` (Code Ocean’s computation snapshot only retains `/results`).
Manuscript notebooks and scripts are under `code/manuscript-2026/`. Optional
notebook re-execution (`RUN_NOTEBOOKS=1`) regenerates embedding-level analyses
**02**, **03**, and **05** and also writes those outputs under `/results`.

**Anonymized intermediates.** Category-level embeddings, detection-prevalence
summaries, main-text result CSVs, and top-8 participant tables
(`participant_01`–`participant_08`) are in
`data/shared_data_manuscript_2026/` (see `MANIFEST.json`). No raw video, crop
paths, or real family identifiers are included. Manuscript numbers from those
analyses can be checked directly against these tables.

**Restricted data.** Per-image crop embeddings, frame-level detection dumps, and
raw egocentric video require BabyView data access under the project’s data-use
agreement. Notebooks that need those assets (**01**, **04**, **08**; Stage 0
embedding builders **06–07**) are documented in [`REPRODUCTION.md`](REPRODUCTION.md)
but are outside the default capsule run.
