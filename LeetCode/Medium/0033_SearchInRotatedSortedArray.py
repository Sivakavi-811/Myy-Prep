"""
LeetCode 33. Search in Rotated Sorted Array (Medium)
https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem:
    A sorted array of distinct integers was rotated at an unknown pivot
    (e.g. [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]). Return the index of `target`,
    or -1, in O(log n) time.

Approach / Intuition:
    Modified binary search. For any mid, at least one half [lo, mid] or
    [mid, hi] is sorted normally. Identify which half is sorted by comparing
    nums[lo] with nums[mid], then check whether the target lies inside that
    sorted half's range. If so, search there; otherwise search the other half.

Complexity:
    Time:  O(log n) - the range halves each step
    Space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:  # left half sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.search([3, 1], 1) == 1
    assert s.search([5, 1, 3], 5) == 0
    print("All test cases passed!")
