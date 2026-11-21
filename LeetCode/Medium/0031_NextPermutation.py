"""
LeetCode 31. Next Permutation (Medium)
https://leetcode.com/problems/next-permutation/

Problem:
    Rearrange nums into the next lexicographically greater permutation, in
    place. If it is already the largest, wrap around to the smallest
    (sorted ascending).

Approach / Intuition:
    1. From the right, find the first index i with nums[i] < nums[i + 1].
       Everything after i is non-increasing - already its largest order.
    2. If such i exists, find the rightmost j > i with nums[j] > nums[i]
       (the smallest value bigger than nums[i] in the suffix) and swap.
    3. Reverse the suffix after i so it becomes its smallest order.
    If no i exists, the whole array is reversed (largest -> smallest).

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from itertools import permutations
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1


if __name__ == "__main__":
    s = Solution()
    for given, expected in [([1, 2, 3], [1, 3, 2]), ([3, 2, 1], [1, 2, 3]),
                            ([1, 1, 5], [1, 5, 1]), ([1], [1])]:
        s.nextPermutation(given)
        assert given == expected

    # Walk all permutations of a multiset in order
    ordered = sorted(set(permutations([1, 2, 2, 3])))
    cur = [1, 2, 2, 3]
    for nxt in ordered[1:]:
        s.nextPermutation(cur)
        assert tuple(cur) == nxt
    print("All test cases passed!")
