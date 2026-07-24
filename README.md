# BabyView Objects — analysis code & reproducibility capsule

Computational reproducibility package for *Characterizing the visual
representation of objects from the child’s view* (Nature Human Behaviour
submission, 2026).

This repository ships analysis source code, a small anonymized demo dataset,
and a fixed compute environment (Code Ocean capsule). The default demo verifies
manuscript tables and does **not** require BabyView video or a GPU.

| Resource | Link |
|----------|------|
| GitHub | https://github.com/babyview-project/babyview-objects-manuscript |
| Code Ocean capsule (provisional DOI) | https://doi.org/10.24433/CO.0860553.v1 |
| Detailed reproduction notes | [`REPRODUCING.md`](REPRODUCING.md) |
| Data & code availability (incl. manuscript text) | [`code/manuscript-2026/DATA_AVAILABILITY.md`](code/manuscript-2026/DATA_AVAILABILITY.md) |

---

## 1. System requirements

### Software

| Component | Requirement |
|-----------|-------------|
| Operating system | macOS or Linux (Windows via WSL2 or Code Ocean) |
| Python | 3.12.x (tested on **3.12.8**) |
| Dependencies | [`code/manuscript-2026/requirements-manuscript.txt`](code/manuscript-2026/requirements-manuscript.txt) (numpy, pandas, scipy, matplotlib, seaborn, scikit-learn, jupyter/nbconvert, tqdm, powerlaw) |

### Versions tested

| Environment | Details |
|-------------|---------|
| Code Ocean base image | `python3.12.8` + Ubuntu 22.04 ([`environment/Dockerfile`](environment/Dockerfile)) |
| Local desktop | macOS 26 (arm64), Apple M3 Pro, Python 3.12.8 |

### Hardware

- **Default demo (`./code/run`):** no non-standard hardware; a normal laptop/desktop with a few GB of free disk is sufficient.
- **Optional / out of scope of this capsule:** GPU and restricted BabyView assets are required only to rebuild embeddings from raw crops/video (Stage 0; notebooks **01**, **04**, **08**). Headline statistics for those analyses are already included as CSVs.

---

## 2. Installation guide

### Option A — Code Ocean (recommended for reviewers)

1. Open the capsule: https://doi.org/10.24433/CO.0860553.v1  
2. Click **Reproducible Run** (entry point: `code/run`).  
3. Inspect `/results`.

No local install is required.

### Option B — Local checkout

```bash
git clone https://github.com/babyview-project/babyview-objects-manuscript.git
cd babyview-objects-manuscript
python3.12 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r code/manuscript-2026/requirements-manuscript.txt
```

**Typical install time** on a normal desktop (fresh venv + `pip install`): about
**1 minute** (measured ≈42 s on an Apple M3 Pro laptop with Python 3.12.8).

---

## 3. Demo

The demo dataset is the anonymized shared tree
[`data/shared_data_manuscript_2026/`](data/shared_data_manuscript_2026/)
(~11 MB; listed in `MANIFEST.json`).

### Instructions

From the repository (or capsule) root:

```bash
./code/run
```

Or, if dependencies are already installed:

```bash
PIP_INSTALL=0 ./code/run
```

### Expected output

On success, the run prints `Reproducible run finished successfully.` and writes:

| Path | Contents |
|------|----------|
| `results/INDEX.txt` | Index of published result files |
| `results/run_summary.txt` | Short run mode summary |
| `results/shared/` | Full copy of `data/shared_data_manuscript_2026/` (71+ files), including main-text CSVs under `results/shared/results_valid129/` |

Example check: open
`results/shared/results_valid129/bv_things_rdm_comparison_summary_filtered-0.27_valid129.csv`
and compare values to the manuscript.

### Expected run time (demo)

On a normal desktop, **under 1 minute** after dependencies are installed
(measured ≈0.4 s for verify + copy on an Apple M3 Pro). Including a fresh
`pip install` inside `./code/run`, expect about **1–2 minutes** total.

Optional: `RUN_NOTEBOOKS=1` also re-executes notebooks **02**, **03**, and **05**
from shipped category embeddings. On a normal desktop this is typically a few
minutes (notebook **05** defaults to 2,000 bootstraps / 5,000 permutations);
see [`REPRODUCING.md`](REPRODUCING.md).

---

## 4. Instructions for use

### Verify manuscript numbers (no recompute)

Compare tables under
`data/shared_data_manuscript_2026/results_valid129/`
to the manuscript. No code execution required.

### Regenerate analyses from shipped embeddings

Category-level embedding tables are included under
`code/manuscript-2026/exemplar_set_embeddings/`. See
[`code/manuscript-2026/REPRODUCTION.md`](code/manuscript-2026/REPRODUCTION.md)
for notebook order, figure ↔ file mapping, and environment variables
(`CATEGORY_SET=valid129|valid85`).

### Run on restricted BabyView data (not in this package)

Rebuilding detections, per-image embeddings, or individual-family RDMs from raw
video requires BabyView data access (Databrary volume
https://www.databrary.org/volume/1882 and the project data-use agreement). Those
steps are documented in
[`code/manuscript-2026/REPRODUCTION.md`](code/manuscript-2026/REPRODUCTION.md)
but are outside the default capsule run; corresponding headline CSVs are still
shipped for verification.

---

## Reproduction of quantitative results

See [`REPRODUCING.md`](REPRODUCING.md) and
[`code/manuscript-2026/REPRODUCTION.md`](code/manuscript-2026/REPRODUCTION.md)
for the full mapping from manuscript figures/analyses to notebooks and CSVs.

---

## License

| Content | License |
|---------|---------|
| Analysis code under `code/` | [MIT](code/LICENSE) (OSI-approved) |
| Anonymized tables under `data/` | [CC0 1.0](data/LICENSE) |

---

## Layout

```text
code/run                          # Reproducible Run / demo entry point
code/manuscript-2026/             # notebooks, scripts, requirements
data/shared_data_manuscript_2026/ # anonymized demo + manuscript tables
environment/                      # Dockerfile + requirements for Code Ocean
results/                          # written by code/run
```
