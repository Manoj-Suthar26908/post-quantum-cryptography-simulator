"""Lightweight memory helper for callable benchmarks."""

import os

import psutil


def measure_memory(func, *args, **kwargs):
    """Return a callable result and resident memory delta in kilobytes."""
    process = psutil.Process(os.getpid())
    before = process.memory_info().rss

    result = func(*args, **kwargs)

    after = process.memory_info().rss
    memory_used_kb = (after - before) / 1024

    return result, memory_used_kb
