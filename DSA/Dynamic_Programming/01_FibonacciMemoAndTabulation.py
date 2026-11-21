"""
DSA - Dynamic Programming 01: Fibonacci (Memoization vs Tabulation)

Problem:
    Compute the n-th Fibonacci number, F(0) = 0, F(1) = 1,
    F(n) = F(n-1) + F(n-2). Used here to compare the core DP techniques.

Approach / Intuition:
    Plain recursion recomputes the same subproblems repeatedly: O(2^n).
    DP fixes that by solving each subproblem once:
      1. Memoization (top-down): recurse as usual, but cache results.
      2. Tabulation (bottom-up): fill a table from the base cases upward.
      3. Space-optimized: each state only needs the previous two, so keep
         just two variables.

Complexity:
    Memoization:     O(n) time, O(n) space (cache + recursion stack)
    Tabulation:      O(n) time, O(n) space (table)
    Space-optimized: O(n) time, O(1) space
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_tab(n: int) -> int:
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib_optimized(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for fn in (fib_memo, fib_tab, fib_optimized):
        assert [fn(i) for i in range(len(expected))] == expected
        assert fn(50) == 12586269025
    print("All test cases passed!")
