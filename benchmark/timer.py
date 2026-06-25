"""Lightweight timing helper for callable benchmarks."""

import time


def measure_time(func, *args, **kwargs):
    """Return a callable result and elapsed wall-clock time in seconds."""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start
