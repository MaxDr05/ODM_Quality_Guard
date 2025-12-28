import pytest

def test_crash_detection(logparse):
    for msg in logparse:
        if "Crash" == msg["category"]:
            assert False
    assert True
    # 拓展写法
    # assert not any(msg["category"] == "Crash" for msg in logparse),"found Crash log!"

def test_memory_leak(logparse):
    for msg in logparse:
        if "Performance" == msg["category"] and "memory leak" == msg["pattern"]:
            assert False
    assert True

    # 拓展写法
    # assert not any(msg["category"] == "Performance" and msg["pattern"] == "memory leak" for msg in logparse),"found memory leak log!"