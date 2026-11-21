"""
LeetCode 54. Spiral Matrix (Medium)
https://leetcode.com/problems/spiral-matrix/

Problem:
    Given an m x n matrix, return all its elements in clockwise spiral order.

Approach / Intuition:
    Keep four boundaries: top, bottom, left, right. Walk the top row left to
    right, the right column downward, the bottom row right to left, and the
    left column upward, shrinking the matching boundary after each side.
    The bottom-row and left-column walks are guarded so a single remaining
    row or column isn't visited twice.

Complexity:
    Time:  O(m * n) - each cell visited once
    Space: O(1) extra besides the output
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out: List[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                out.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                out.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    out.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    out.append(matrix[i][left])
                left += 1
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert s.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert s.spiralOrder([[1, 2, 3]]) == [1, 2, 3]
    print("All test cases passed!")
