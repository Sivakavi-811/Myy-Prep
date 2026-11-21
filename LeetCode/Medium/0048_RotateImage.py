"""
LeetCode 48. Rotate Image (Medium)
https://leetcode.com/problems/rotate-image/

Problem:
    Rotate an n x n matrix 90 degrees clockwise, in place.

Approach / Intuition:
    A clockwise rotation equals a transpose (swap matrix[i][j] with
    matrix[j][i]) followed by reversing each row. Both steps are simple
    in-place operations, avoiding the four-way index juggling of rotating
    ring by ring.

Complexity:
    Time:  O(n^2) - every cell touched a constant number of times
    Space: O(1)
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    s = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(m)
    assert m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    m = [[1]]
    s.rotate(m)
    assert m == [[1]]
    print("All test cases passed!")
