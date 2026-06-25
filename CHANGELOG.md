# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project follows semantic versioning where practical.

## [Unreleased]

### Added

- Professional repository documentation and community files.
- MIT license.
- GitHub issue templates and pull request template.
- GitHub Actions workflow for formatting, linting, and tests.
- Falcon-512 and SPHINCS+-SHA2-128f benchmark wrappers.
- Basic smoke tests for imports and benchmark aggregation.

### Changed

- Dockerfile now installs dependencies from `requirements.txt`.
- Benchmark standard deviation now supports single-run smoke tests.
- Plot generation now writes relative to the provided CSV path.

### Removed

- Empty duplicate plotting script.
- Local cache and virtual environment artifacts from the working tree.
