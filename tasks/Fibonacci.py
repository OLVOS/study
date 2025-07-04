

def fib(n):
    if n < 1:
        return 0
    first, second = 0, 1
    n_without_firts_two = n - 1
    for _ in range(n_without_firts_two):
        first, second = second, first
        second = first + second

    return second


def test_fibonacci():

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
