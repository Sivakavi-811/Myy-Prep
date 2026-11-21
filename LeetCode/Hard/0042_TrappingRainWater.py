"""
LeetCode 42. Trapping Rain Water (Hard)
https://leetcode.com/problems/trapping-rain-water/

Problem:
    Given n non-negative integers representing an elevation map where each
    bar has width 1, compute how much water it can trap after raining.

Approach / Intuition:
    Water above bar i = min(max height to its left, max height to its
    right) - height[i]. Two pointers avoid storing both max arrays:
    keep left_max and right_max. Whichever side has the smaller max is the
    bottleneck - its water level is fully determined by that side's max,
    regardless of what lies between the pointers. Process that side and
    move its pointer inward.

Complexity:
    Time:  O(n) - pointers meet after one pass
    Space: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
    assert s.trap([]) == 0
    assert s.trap([3, 2, 1]) == 0
    print("All test cases passed!")
