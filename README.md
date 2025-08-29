# datafun-01-utils
First Repo
# datafun-01-utils · Reusable Tagline Module

A small, professional Python module that builds and prints a reusable **project tagline/header** for analytics projects. It’s cleanly typed, includes a CLI, runs a self-check, and can optionally read the tagline aloud.

> Main module: `utils_sandra_otubushin.py`

---

## Why this exists

- Provide a consistent, informative header across projects.
- Practice professional Python structure (types, CLI, logging, tests).
- Offer a tiny public API (`get_tagline()`) that you can import anywhere.

---

## Features

- **Public API**: `get_tagline()` and `read_tagline_aloud()`
- **CLI flags**:
  - `--check` → quick self-test of calculations and output
  - `--speak` → optional text-to-speech (if `pyttsx3` installed)
- **Graceful fallbacks** if `loguru`/`pyttsx3` are missing
- **Typed globals**, computed statistics, neat formatted header

---

## Requirements

- Python 3.10+ (works fine in a venv)
- Packages listed in `requirements.txt` (e.g., `loguru`, `pyttsx3`)

Install:

```bash
pip install -r requirements.txt
