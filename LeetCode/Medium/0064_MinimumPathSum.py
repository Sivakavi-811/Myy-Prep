"""
LeetCode 64. Minimum Path Sum (Medium)
https://leetcode.com/problems/minimum-path-sum/

Problem:
    Given an m x n grid of non-negative numbers, find a path from the
    top-left to the bottom-right (moving only right or down) that minimizes
    the sum of the numbers along it.

Approach / Intuition:
    The cheapest way into a cell comes from either the cell above or the
    cell to the left:
        dp[j] = grid[i][j] + min(dp[j] (above), dp[j - 1] (left))
    The first row can only be reached from the left, and the first column
    only from above. A single row array updated in place suffices.

Complexity:
    Time:  O(m * n)
    Space: O(n)
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [0] * n
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i == 0 and j == 0:
                    dp[j] = val
                elif i == 0:
                    dp[j] = dp[j - 1] + val
                elif j == 0:
                    dp[j] = dp[j] + val
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + val
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert s.minPathSum([[5]]) == 5
    assert s.minPathSum([[1], [2], [3]]) == 6
    print("All test cases passed!")
