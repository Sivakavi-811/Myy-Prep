"""
LeetCode 62. Unique Paths (Medium)
https://leetcode.com/problems/unique-paths/

Problem:
    A robot starts at the top-left of an m x n grid and can only move right
    or down. How many unique paths reach the bottom-right corner?

Approach / Intuition:
    DP: paths into a cell = paths from above + paths from the left. The
    first row and column have exactly one path each. Only the previous row
    is needed, so a 1-D array updated in place suffices:
        row[j] += row[j - 1]
    (Closed form: choose which (m-1) of the (m+n-2) moves go down,
    C(m+n-2, m-1) - used in the tests as a cross-check.)

Complexity:
    Time:  O(m * n)
    Space: O(n)
"""

from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(1, 1) == 1
    for m, n in [(10, 10), (23, 12), (1, 50)]:
        assert s.uniquePaths(m, n) == comb(m + n - 2, m - 1)
    print("All test cases passed!")
