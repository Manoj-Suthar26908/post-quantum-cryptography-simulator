# Contributing

Thank you for considering a contribution to Post-Quantum Cryptography Simulator.

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest ruff
```

## Workflow

1. Create a focused branch.
2. Keep changes scoped to one feature, fix, or documentation improvement.
3. Add or update tests when behavior changes.
4. Run the checks locally:

```bash
ruff format --check .
ruff check .
pytest
```

5. Open a pull request using the PR template.

## Code Guidelines

- Keep cryptographic wrappers small and explicit.
- Do not introduce custom cryptographic primitives.
- Prefer well-maintained libraries for algorithm implementations.
- Document new algorithms with parameter set names and source libraries.
- Keep generated results out of version control.

## Reporting Bugs

Use the bug report issue template and include:

- operating system
- Python version
- dependency versions
- command run
- full traceback or output
