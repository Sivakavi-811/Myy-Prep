"""
DSA - Dynamic Programming 06: Matrix Chain Multiplication

Problem:
    Given dimensions dims where matrix i has size dims[i-1] x dims[i],
    find the minimum number of scalar multiplications needed to compute the
    product A1 * A2 * ... * An, and the optimal parenthesization.

Approach / Intuition:
    Interval DP. cost[i][j] = cheapest way to multiply matrices i..j.
    Try every split point k (multiply i..k and k+1..j, then the two results):
        cost[i][j] = min over k of
            cost[i][k] + cost[k+1][j] + dims[i-1] * dims[k] * dims[j]
    Fill by increasing chain length so sub-intervals are ready first.
    Store the best k to rebuild the parenthesization.
    Order matters a lot: (10x30)(30x5)(5x60) costs 4500 one way, 27000 the
    other.

Complexity:
    Time:  O(n^3)
    Space: O(n^2)
"""

from typing import List, Tuple


def matrix_chain(dims: List[int]) -> Tuple[int, str]:
    n = len(dims) - 1
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            cost[i][j] = float("inf")
            for k in range(i, j):
                c = cost[i][k] + cost[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if c < cost[i][j]:
                    cost[i][j], split[i][j] = c, k

    def paren(i: int, j: int) -> str:
        if i == j:
            return f"A{i}"
        k = split[i][j]
        return f"({paren(i, k)}{paren(k + 1, j)})"

    return (cost[1][n], paren(1, n)) if n >= 1 else (0, "")


if __name__ == "__main__":
    assert matrix_chain([10, 30, 5, 60]) == (4500, "((A1A2)A3)")
    assert matrix_chain([40, 20, 30, 10, 30])[0] == 26000
    assert matrix_chain([1, 2, 3, 4, 3])[0] == 30
    assert matrix_chain([10, 20]) == (0, "A1")
    print("All test cases passed!")
