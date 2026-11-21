"""
LeetCode 128. Longest Consecutive Sequence (Medium)
https://leetcode.com/problems/longest-consecutive-sequence/

Problem:
    Given an unsorted integer array, return the length of the longest run
    of consecutive integers (e.g. 1, 2, 3, 4). Must run in O(n).

Approach / Intuition:
    Put everything in a set for O(1) lookups. Only start counting from
    numbers that begin a sequence - those where (x - 1) is NOT in the set.
    From each start, count upward while x + 1 exists. Each number is part
    of exactly one upward walk, so the total work stays linear.

Complexity:
    Time:  O(n) - every element is visited at most twice
    Space: O(n) - the set
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        best = 0
        for x in values:
            if x - 1 not in values:
                length = 1
                while x + length in values:
                    length += 1
                best = max(best, length)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    assert s.longestConsecutive([1, 2, 0, 1]) == 3
    print("All test cases passed!")
