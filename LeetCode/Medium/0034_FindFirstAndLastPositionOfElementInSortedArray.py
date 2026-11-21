"""
LeetCode 34. Find First and Last Position of Element in Sorted Array (Medium)
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Problem:
    Given a sorted array and a target, return [first, last] indices of the
    target, or [-1, -1] if absent. Must run in O(log n).

Approach / Intuition:
    Two lower-bound binary searches:
      first = lower_bound(target)       (first index with value >= target)
      last  = lower_bound(target + 1) - 1
    If `first` is out of range or doesn't hold target, it isn't present.
    Reusing one helper avoids writing two subtly different searches.

Complexity:
    Time:  O(log n)
    Space: O(1)
"""

from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = lower_bound(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, lower_bound(nums, target + 1) - 1]


if __name__ == "__main__":
    s = Solution()
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert s.searchRange([], 0) == [-1, -1]
    assert s.searchRange([2, 2], 2) == [0, 1]
    assert s.searchRange([1], 1) == [0, 0]
    print("All test cases passed!")
