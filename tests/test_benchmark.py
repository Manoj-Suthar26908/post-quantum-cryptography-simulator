from benchmark.benchmark import benchmark_algorithm


def test_benchmark_algorithm_supports_single_run():
    def sample_algorithm():
        return {
            "success": True,
            "public_key_size": 10,
            "private_key_size": 20,
            "data_size": 30,
        }

    result = benchmark_algorithm("sample", sample_algorithm, runs=1)

    assert result["Algorithm"] == "sample"
    assert result["Success"] is True
    assert result["Std_Dev_Time"] == 0.0
    assert result["Public_Key_Size"] == 10
