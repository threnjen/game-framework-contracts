# Local Development

## Prerequisites

- Python 3.12 or newer
- `pip`
- Optional: `make`

## Setup

1. Create a virtual environment.
2. Activate it.
3. Install the package in editable mode.
4. Install the tooling needed for packaging and tests.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install build pytest
```

## Common Commands

### Install

- Editable install: `python -m pip install -e .`
- Build toolchain: `python -m pip install build pytest`

### Package

- Build sdists and wheels: `make package`
- Equivalent direct command: `python -m build --sdist --wheel --outdir dist`

### Test

- Run tests: `make test`
- Equivalent direct command: `python -m pytest -q`

## What To Expect

- `make venv` creates `.venv` and ensures `build` is installed.
- `make package` writes artifacts to `dist/`.
- `make test` assumes `pytest` is available in the virtual environment.
- The repository currently contains contract modules rather than executable application code, so setup verification is mostly import and packaging oriented.