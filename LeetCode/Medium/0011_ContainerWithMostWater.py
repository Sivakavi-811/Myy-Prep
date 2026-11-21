"""
LeetCode 11. Container With Most Water (Medium)
https://leetcode.com/problems/container-with-most-water/

Problem:
    Given heights of n vertical lines, pick two lines that, together with
    the x-axis, form a container holding the most water. Return that area.

Approach / Intuition:
    Two pointers at both ends (widest container). Area = width * min height.
    Moving the taller line inward can never help: the width shrinks and the
    height is still capped by the shorter line. So always move the shorter
    line, which is the only move that might find a taller boundary.

Complexity:
    Time:  O(n) - pointers meet after n - 1 moves
    Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        best = 0
        while i < j:
            best = max(best, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([4, 3, 2, 1, 4]) == 16
    print("All test cases passed!")
