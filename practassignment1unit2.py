import timeit


# 1. Iterative DP (Recommended / O(n) Time, O(1) Space)
def fib_dp(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# 2. Fast Doubling (O(log n) Time)
def fib_fast_doubling(n):
    def _fib_pair(k):
        if k == 0:
            return (0, 1)
        a, b = _fib_pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return _fib_pair(n)[0]


# 3. Memoized Recursion (O(n) Time)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    n = 100

    print(f"Computing Fibonacci({n}):\n")
    print(f"[1] Iterative DP   : {fib_dp(n)}")
    print(f"[2] Fast Doubling  : {fib_fast_doubling(n)}")
    print(f"[3] Memoized DP    : {fib_memo(n)}")

    # Timing comparison between fast methods
    t_dp = timeit.timeit(lambda: fib_dp(n), number=10000)
    t_fast = timeit.timeit(lambda: fib_fast_doubling(n), number=10000)

    print(f"\nTiming for 10,000 runs:")
    print(f"  Iterative DP  : {t_dp:.6f} sec")
    print(f"  Fast Doubling : {t_fast:.6f} sec")