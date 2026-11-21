"""
LeetCode 74. Search a 2D Matrix (Medium)
https://leetcode.com/problems/search-a-2d-matrix/

Problem:
    Each row of an m x n matrix is sorted, and each row's first value is
    greater than the previous row's last value. Return True if target is
    in the matrix, in O(log(m * n)).

Approach / Intuition:
    Read row by row, the matrix is one sorted list of m * n values. Binary
    search over virtual indices 0..m*n-1, mapping index k to
    matrix[k // n][k % n]. No flattening needed.

Complexity:
    Time:  O(log(m * n))
    Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(matrix, 3) is True
    assert s.searchMatrix(matrix, 13) is False
    assert s.searchMatrix(matrix, 60) is True
    assert s.searchMatrix(matrix, 1) is True
    assert s.searchMatrix([[1]], 2) is False
    print("All test cases passed!")
