# Manuscript helper scripts

Runnable `.py` helpers for statistics, supplement CLIs, and the Code Ocean
reproduce path. **`manuscript_config.py` stays in the parent folder** so notebooks
can `from manuscript_config import ...` with cwd = `code/manuscript-2026/`.

```bash
# from code/manuscript-2026/
python scripts/verify_shared_data.py --strict
CATEGORY_SET=valid129 python scripts/reproduce_capsule.py
```

Full catalog: **[../SCRIPTS.md](../SCRIPTS.md)**. Capsule entry point: **[`../../run`](../../run)**.

Imports between scripts use [`_bootstrap.py`](_bootstrap.py) (`MANUSCRIPT_DIR`, `SCRIPTS_DIR`, `PROJECT_ROOT`).
