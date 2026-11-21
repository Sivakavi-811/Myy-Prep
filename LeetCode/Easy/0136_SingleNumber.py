"""
LeetCode 136. Single Number (Easy)
https://leetcode.com/problems/single-number/

Problem:
    Every element in a non-empty integer array appears twice except for one.
    Find that single one, using linear time and constant extra space.

Approach / Intuition:
    XOR has three useful properties: x ^ x = 0, x ^ 0 = x, and it is
    commutative/associative. XOR-ing the whole array cancels every pair,
    leaving only the unique element.

Complexity:
    Time:  O(n) - one pass
    Space: O(1) - a single accumulator
"""

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1
    assert s.singleNumber([-3, 7, 7]) == -3
    print("All test cases passed!")
