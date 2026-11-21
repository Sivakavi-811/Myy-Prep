"""
LeetCode 118. Pascal's Triangle (Easy)
https://leetcode.com/problems/pascals-triangle/

Problem:
    Given numRows, return the first numRows rows of Pascal's triangle,
    where each number is the sum of the two numbers directly above it.

Approach / Intuition:
    Each row starts and ends with 1. The interior entries of row i are
    pairwise sums of adjacent entries in row i - 1. Build row by row.

Complexity:
    Time:  O(numRows^2) - total number of entries
    Space: O(numRows^2) - the output itself
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows: List[List[int]] = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
            rows.append(row)
        return rows


if __name__ == "__main__":
    s = Solution()
    assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert s.generate(1) == [[1]]
    assert s.generate(0) == []
    print("All test cases passed!")
