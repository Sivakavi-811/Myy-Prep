"""
LeetCode 349. Intersection of Two Arrays (Easy)
https://leetcode.com/problems/intersection-of-two-arrays/

Problem:
    Given two integer arrays, return their intersection. Each element of
    the result must be unique; order doesn't matter.

Approach / Intuition:
    Convert the smaller array to a set (less memory), then keep the
    distinct elements of the other array that appear in it. Set lookups
    are O(1) on average.

Complexity:
    Time:  O(m + n)
    Space: O(min(m, n)) - the set of the smaller array
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        small = set(nums1)
        return list(small.intersection(nums2))


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(s.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert s.intersection([1], [2]) == []
    print("All test cases passed!")
