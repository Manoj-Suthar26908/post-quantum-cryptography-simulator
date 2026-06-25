# Post-Quantum Cryptography Simulator

A Python benchmarking simulator for comparing classical RSA with post-quantum cryptography algorithms. The project measures execution time, memory delta, key sizes, and ciphertext/signature sizes, then exports CSV results and comparison plots.

This repository is intended for cybersecurity learning, portfolio review, and contributor-friendly experimentation. It is not a production cryptography library and should not be used to secure real systems.

## Features

- Benchmarks classical and post-quantum algorithms through a consistent interface.
- Generates CSV output for repeatable performance analysis.
- Produces matplotlib charts for timing and data-size comparison.
- Includes Docker support for reproducible execution.
- Provides GitHub issue templates, contribution guidelines, security policy, changelog, tests, and CI.

## Architecture

The simulator is organized around small modules with single responsibilities:

- `main.py` orchestrates the benchmark run and writes result files.
- `pqc/` contains post-quantum algorithm wrappers backed by `pqcrypto`.
- `classical/` contains RSA baseline logic backed by `cryptography`.
- `benchmark/` contains timing, memory, and aggregate benchmark utilities.
- `analysis/` converts benchmark CSV output into plots.
- `tests/` contains smoke tests for imports and benchmark aggregation behavior.

## Supported Algorithms

| Algorithm | Category | Implementation |
| --- | --- | --- |
| CRYSTALS-Kyber / ML-KEM-512 | Key encapsulation | `pqcrypto.kem.ml_kem_512` |
| CRYSTALS-Dilithium / ML-DSA-44 | Digital signature | `pqcrypto.sign.ml_dsa_44` |
| Falcon-512 | Digital signature | `pqcrypto.sign.falcon_512` |
| SPHINCS+-SHA2-128f | Stateless hash-based signature | `pqcrypto.sign.sphincs_sha2_128f_simple` |
| RSA-2048 | Classical baseline | `cryptography` |

## Benchmarking Module

`benchmark.benchmark_algorithm()` runs each algorithm multiple times and records:

- average execution time in seconds
- standard deviation of execution time
- average memory delta in KB
- public key size
- private key size
- ciphertext or signature size
- success status

By default, each algorithm is run 50 times.

## Performance Analysis

After running the simulator, output is written to `results/results.csv` and plots are generated in `results/`:

- `time_all.png`
- `time_pqc.png`
- `time_kyber.png`
- `size_all.png`
- `size_pqc.png`
- `size_kyber.png`

These files are generated artifacts and are ignored by Git.

## Project Structure

```text
post-quantum-cryptography-simulator/
├── analysis/
├── benchmark/
├── classical/
├── pqc/
├── plots/
├── docs/
├── screenshots/
├── tests/
├── Dockerfile
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── .gitignore
└── .github/
    ├── workflows/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## Installation

```bash
git clone https://github.com/<your-username>/post-quantum-cryptography-simulator.git
cd post-quantum-cryptography-simulator
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Requirements

- Python 3.11+
- `cryptography`
- `pqcrypto`
- `pandas`
- `matplotlib`
- `psutil`

## Usage

Run the full benchmark suite:

```bash
python main.py
```

Use an individual algorithm wrapper:

```python
from pqc.kyber import kyber_test

result = kyber_test()
print(result)
```

Run tests:

```bash
pip install pytest
pytest
```

## Docker Usage

This repository includes a `Dockerfile`.

```bash
docker build -t post-quantum-cryptography-simulator .
docker run --rm post-quantum-cryptography-simulator
```

## Screenshots

Add screenshots of generated charts or terminal output to `screenshots/` before publishing the repository. Recommended screenshots:

- terminal benchmark run
- timing comparison plot
- size comparison plot

## Future Improvements

- Add command-line flags for selecting algorithms and run counts.
- Export benchmark results as JSON in addition to CSV.
- Add richer plots for key size, signature size, and memory usage.
- Add automated benchmark history for release comparisons.
- Package the simulator as an installable Python project.
- Add more parameter sets for ML-KEM, ML-DSA, Falcon, and SPHINCS+.

## Authors

Maintained by the Post-Quantum Cryptography Simulator contributors.

## License

MIT is recommended for this project because it is permissive, familiar to open-source contributors, and appropriate for educational tooling. See [LICENSE](LICENSE).
