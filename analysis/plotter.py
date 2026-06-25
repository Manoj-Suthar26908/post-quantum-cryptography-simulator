"""Plot benchmark CSV output as comparison charts."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def generate_plots(csv_path):
    """Generate execution-time and data-size plots from a benchmark CSV file."""
    output_dir = Path(csv_path).parent
    output_dir.mkdir(exist_ok=True)
    df = pd.read_csv(csv_path)

    pqc_df = df[df["Algorithm"].str.contains("Kyber|Dilithium|Falcon|SPHINCS")]
    kyber_df = df[df["Algorithm"].str.contains("Kyber")]

    plt.figure()
    plt.bar(df["Algorithm"], df["Avg_Time_sec"])
    plt.title("Execution Time: All Algorithms")
    plt.xlabel("Algorithm")
    plt.ylabel("Average Time (sec)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_dir / "time_all.png")
    plt.close()

    plt.figure()
    plt.bar(pqc_df["Algorithm"], pqc_df["Avg_Time_sec"])
    plt.title("Execution Time: Post-Quantum Algorithms")
    plt.xlabel("Algorithm")
    plt.ylabel("Average Time (sec)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_dir / "time_pqc.png")
    plt.close()

    plt.figure()
    plt.bar(kyber_df["Algorithm"], kyber_df["Avg_Time_sec"])
    plt.title("Execution Time: Kyber Only")
    plt.xlabel("Algorithm")
    plt.ylabel("Average Time (sec)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_dir / "time_kyber.png")
    plt.close()

    plt.figure()
    plt.bar(df["Algorithm"], df["Data_Size"])
    plt.title("Data Size: All Algorithms")
    plt.xlabel("Algorithm")
    plt.ylabel("Data Size (Bytes)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_dir / "size_all.png")
    plt.close()

    plt.figure()
    plt.bar(pqc_df["Algorithm"], pqc_df["Data_Size"])
    plt.title("Data Size: Post-Quantum Algorithms")
    plt.xlabel("Algorithm")
    plt.ylabel("Data Size (Bytes)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_dir / "size_pqc.png")
    plt.close()

    plt.figure()
    plt.bar(kyber_df["Algorithm"], kyber_df["Data_Size"])
    plt.title("Data Size: Kyber Only")
    plt.xlabel("Algorithm")
    plt.ylabel("Data Size (Bytes)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_dir / "size_kyber.png")
    plt.close()

    print("All performance graphs generated successfully.")
