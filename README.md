# BabyView Objects — manuscript capsule

Slim, **manuscript-only** export for CodeOcean / public redistribution.
This is **not** the full internal monorepo.

Generated from: `object-detection` at 2026-07-15T03:08Z  
Profile: **manuscript** (figures=0, exemplar=1, vqa_summary=1, stage0=0)

## Layout

```text
analysis/manuscript-2026/          # notebooks 01–05, 08–10 + analysis scripts
analysis/manuscript-2026/exemplar_set_embeddings/   # z-scored category tables (Tier B)
data/shared_data_manuscript_2026/  # anonymized Tier A tables (MANIFEST.json)
data/shared_data_manuscript_2026/vqa_detections/    # YOLOE↔VQA SI summaries + figures
data/included_categories_*.txt, cdi_words.csv, …
```

## Quick start

```bash
pip install -r analysis/manuscript-2026/requirements-manuscript.txt
```

1. Verify published aggregates under `data/shared_data_manuscript_2026/results_valid129/`.
2. YOLOE↔VQA frame-prevalence correlation: `vqa_detections/yoloe_vqa_correlation.json`
   and `vqa_detections/figures/vqa_comparison_frame_prevalence.*`.
3. Read `analysis/manuscript-2026/REPRODUCTION.md` for notebook order.
4. (Optional) Rerun notebooks **01–05 / 08–10** with cwd = `analysis/manuscript-2026/`.

## Intentionally not included

- Stage 0 GPU/tmux builders (notebooks 06–07, `run_*_tmux.sh`, crop embedding scripts)
- `not_in_manuscript/`, other conference pilots, YOLOE / raw video / per-crop `.npy`
- Local `main_results/` trees with real subject IDs (use anonymized `shared_data_…/top8_valid85/`)
- Video-level VQA dump `unconstrained_objects.csv` (has `video_id`; use `--include-vqa-raw` only if needed)

Full Stage 0 rebuild from crops requires BabyView data access (documented in the monorepo).

## CodeOcean

- Upload this directory as the capsule root (`analysis/` and `data/` as siblings).
- Point the reproducible run at Tier A verification and/or selected notebooks — not GPU re-embedding.

## License / data use

Only anonymized tables under `data/shared_data_manuscript_2026/` are intended for
public redistribution. Respect BabyView data-use agreements for any restricted assets.
