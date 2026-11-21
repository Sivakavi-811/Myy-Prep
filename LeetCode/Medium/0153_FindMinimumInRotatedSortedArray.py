"""
LeetCode 153. Find Minimum in Rotated Sorted Array (Medium)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Problem:
    A sorted array of unique values was rotated between 1 and n times.
    Return its minimum element in O(log n).

Approach / Intuition:
    Compare nums[mid] with nums[hi]. If nums[mid] > nums[hi], the rotation
    point (the minimum) lies strictly to the right of mid. Otherwise the
    segment mid..hi is sorted, so the minimum is at mid or to its left.
    Shrink until lo == hi.

Complexity:
    Time:  O(log n)
    Space: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    assert s.findMin([2, 1]) == 1
    assert s.findMin([5]) == 5
    print("All test cases passed!")
