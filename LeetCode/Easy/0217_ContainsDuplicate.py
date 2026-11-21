"""
LeetCode 217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Problem:
    Given an integer array `nums`, return True if any value appears at least
    twice, and False if every element is distinct.

Approach / Intuition:
    Keep a hash set of values seen so far. While scanning, if the current
    value is already in the set we have found a duplicate and can stop early.
    Alternatives:
      - Sort, then compare neighbours: O(n log n) time, O(1) extra space.
      - len(set(nums)) != len(nums): concise, but always scans everything.
    The early-exit set approach is the best balance in practice.

Complexity:
    Time:  O(n)  - one pass with O(1) average set operations
    Space: O(n)  - the set may hold all n elements
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert s.containsDuplicate([5]) is False
    print("All test cases passed!")
