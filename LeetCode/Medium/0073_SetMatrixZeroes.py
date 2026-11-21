"""
LeetCode 73. Set Matrix Zeroes (Medium)
https://leetcode.com/problems/set-matrix-zeroes/

Problem:
    If an element of an m x n matrix is 0, set its entire row and column to
    0. Do it in place, ideally with O(1) extra space.

Approach / Intuition:
    Use the first row and first column as marker storage: when
    matrix[i][j] == 0, set matrix[i][0] = matrix[0][j] = 0. The first row
    and column then can't record their own zeros, so remember those in two
    booleans first. Zero the inner cells from the markers, then handle the
    first row/column last so the markers aren't destroyed too early.

Complexity:
    Time:  O(m * n)
    Space: O(1)
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    s = Solution()
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(m)
    assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    m = [[1, 0]]
    s.setZeroes(m)
    assert m == [[0, 0]]
    print("All test cases passed!")
