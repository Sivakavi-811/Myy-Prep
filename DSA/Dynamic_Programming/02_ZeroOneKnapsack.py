"""
DSA - Dynamic Programming 02: 0/1 Knapsack

Problem:
    Given n items with weights w[i] and values v[i], and a bag of capacity W,
    choose a subset (each item at most once) with total weight <= W that
    maximizes total value.

Approach / Intuition:
    dp[i][c] = best value using the first i items with capacity c.
    For item i we either skip it or take it (if it fits):
        dp[i][c] = max(dp[i-1][c], dp[i-1][c - w[i]] + v[i])
    Space optimization: keep one row and iterate capacity from HIGH to LOW,
    so dp[c - w] still holds the previous item's value - this is what
    prevents using the same item twice. (Iterating low to high would give
    the unbounded knapsack instead.)

Complexity:
    Time:  O(n * W)
    Space: O(W) with the 1-D table
"""

from typing import List


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


if __name__ == "__main__":
    assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert knapsack([10, 20, 30], [60, 100, 120], 50) == 220
    assert knapsack([5], [10], 4) == 0
    assert knapsack([], [], 10) == 0
    # each item at most once: unbounded would answer 30 here
    assert knapsack([1], [10], 3) == 10
    print("All test cases passed!")
