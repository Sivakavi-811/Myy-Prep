"""
LeetCode 1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Problem:
    Given an array of integers `nums` and an integer `target`, return the
    indices of the two numbers that add up to `target`. Exactly one solution
    exists, and the same element may not be used twice.

Approach / Intuition:
    For each number x, the partner we need is (target - x). Instead of
    searching for it with a nested loop (O(n^2)), keep a hash map of
    value -> index for everything seen so far. As we scan, check whether
    the complement is already in the map; if so, we have the answer.
    Checking before inserting guarantees we never pair an element with itself.

Complexity:
    Time:  O(n)  - single pass, O(1) average hash-map lookups
    Space: O(n)  - the hash map may store up to n entries
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # unreachable per problem guarantees


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("All test cases passed!")
