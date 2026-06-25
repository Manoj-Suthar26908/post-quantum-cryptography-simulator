"""Command-line entry point for the Post-Quantum Cryptography Simulator."""

import csv
from pathlib import Path

from analysis.plotter import generate_plots
from benchmark.benchmark import benchmark_algorithm
from classical.rsa import rsa_test
from pqc.dilithium import dilithium_test
from pqc.falcon import falcon_test
from pqc.kyber import kyber_test
from pqc.sphincs import sphincs_test

RESULTS_DIR = Path("results")
RESULTS_FILE = RESULTS_DIR / "results.csv"


def main():
    """Run all configured algorithm benchmarks and generate result plots."""
    print("\n==============================")
    print("POST-QUANTUM CRYPTO SIMULATOR")
    print("==============================")

    RESULTS_DIR.mkdir(exist_ok=True)
    benchmarks = [
        ("RSA-2048", rsa_test),
        ("Kyber-512", kyber_test),
        ("Dilithium-2", dilithium_test),
        ("Falcon-512", falcon_test),
        ("SPHINCS+-SHA2-128f", sphincs_test),
    ]

    results = []
    for name, test_function in benchmarks:
        print(f"\nRunning {name} Benchmark...")
        results.append(benchmark_algorithm(name, test_function))

    with RESULTS_FILE.open("w", newline="") as csvfile:
        fieldnames = [
            "Algorithm",
            "Success",
            "Avg_Time_sec",
            "Std_Dev_Time",
            "Avg_Memory_KB",
            "Public_Key_Size",
            "Private_Key_Size",
            "Data_Size",
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\nBenchmark completed successfully.")
    print(f"Results saved to {RESULTS_FILE}")

    generate_plots(RESULTS_FILE)


if __name__ == "__main__":
    main()
