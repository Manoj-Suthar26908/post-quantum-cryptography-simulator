# Architecture

The simulator follows a simple pipeline:

1. Algorithm wrappers perform one cryptographic operation cycle and return standardized metrics.
2. The benchmark module repeats each wrapper and aggregates timing, memory, and size data.
3. `main.py` writes a CSV report.
4. The analysis module reads the CSV and generates plots.

This keeps cryptographic behavior isolated from reporting and plotting code.
