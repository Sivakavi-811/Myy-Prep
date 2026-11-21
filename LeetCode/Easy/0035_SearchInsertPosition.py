"""
LeetCode 35. Search Insert Position (Easy)
https://leetcode.com/problems/search-insert-position/

Problem:
    Given a sorted array of distinct integers and a target, return the index
    of the target if found, otherwise the index where it would be inserted
    to keep the array sorted. Must run in O(log n).

Approach / Intuition:
    This is "lower bound": the first index whose value is >= target.
    Binary search on the half-open range [lo, hi): if nums[mid] < target,
    the answer is to the right of mid; otherwise mid itself could be the
    answer, so keep it. When lo == hi, that is the insertion point.

Complexity:
    Time:  O(log n)
    Space: O(1)
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    assert s.searchInsert([], 3) == 0
    print("All test cases passed!")
