"""
DSA - Dynamic Programming 05: Longest Increasing Subsequence (LIS)

Problem:
    Given an array, return the length of the longest strictly increasing
    subsequence (not necessarily contiguous).

Approach / Intuition:
    1. O(n^2) DP: dp[i] = LIS ending at i = 1 + max(dp[j]) over j < i with
       arr[j] < arr[i]. Easy to reason about and to reconstruct.
    2. O(n log n) "patience sorting": tails[k] holds the smallest possible
       tail of an increasing subsequence of length k + 1. tails stays
       sorted, so for each x, binary-search the first tail >= x and replace
       it (a smaller tail is never worse); if x beats every tail, append.
       len(tails) is the answer (tails itself is not necessarily an LIS).

Complexity:
    DP:        O(n^2) time, O(n) space
    Patience:  O(n log n) time, O(n) space
"""

from bisect import bisect_left
from typing import List


def lis_dp(arr: List[int]) -> int:
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_fast(arr: List[int]) -> int:
    tails: List[int] = []
    for x in arr:
        k = bisect_left(tails, x)
        if k == len(tails):
            tails.append(x)
        else:
            tails[k] = x
    return len(tails)


if __name__ == "__main__":
    cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([], 0),
        ([5, 4, 3, 2, 1], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ]
    for arr, expected in cases:
        assert lis_dp(arr) == expected
        assert lis_fast(arr) == expected
    print("All test cases passed!")
