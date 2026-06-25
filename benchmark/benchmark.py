"""Benchmark utilities for timing, memory, and output-size comparisons."""

import os
import statistics
import time

import psutil


def benchmark_algorithm(name, test_function, runs=50):
    """Run an algorithm test repeatedly and return aggregate metrics."""
    times = []
    memories = []

    public_key_sizes = []
    private_key_sizes = []
    data_sizes = []
    result = None

    for _ in range(runs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss

        start = time.perf_counter()
        result = test_function()
        end = time.perf_counter()

        mem_after = process.memory_info().rss

        times.append(end - start)
        memories.append((mem_after - mem_before) / 1024)

        public_key_sizes.append(result["public_key_size"])
        private_key_sizes.append(result["private_key_size"])
        data_sizes.append(result["data_size"])

    if result is None:
        raise ValueError("runs must be greater than zero")

    return {
        "Algorithm": name,
        "Success": result["success"],
        "Avg_Time_sec": statistics.mean(times),
        "Std_Dev_Time": statistics.stdev(times) if len(times) > 1 else 0.0,
        "Avg_Memory_KB": statistics.mean(memories),
        "Public_Key_Size": statistics.mean(public_key_sizes),
        "Private_Key_Size": statistics.mean(private_key_sizes),
        "Data_Size": statistics.mean(data_sizes),
    }
