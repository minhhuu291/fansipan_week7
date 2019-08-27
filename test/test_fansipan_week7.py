from fansipan_week7 import fansipan_week7


def test_fib() -> None:
    assert fansipan_week7.fib(0) == 0
    assert fansipan_week7.fib(1) == 1
    assert fansipan_week7.fib(2) == 1
    assert fansipan_week7.fib(3) == 2
    assert fansipan_week7.fib(4) == 3
    assert fansipan_week7.fib(5) == 5
    assert fansipan_week7.fib(10) == 55
