"""
LeetCode 268. Missing Number (Easy)
https://leetcode.com/problems/missing-number/

Problem:
    Given an array containing n distinct numbers from the range [0, n],
    return the only number in that range missing from the array.

Approach / Intuition:
    XOR every index 0..n with every value in the array. Each number that is
    present appears twice (once as an index, once as a value) and cancels
    out, leaving only the missing number. Unlike the sum formula
    n(n+1)/2 - sum(nums), XOR can't overflow in fixed-width languages.

Complexity:
    Time:  O(n) - one pass
    Space: O(1)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, x in enumerate(nums):
            result ^= i ^ x
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert s.missingNumber([1]) == 0
    print("All test cases passed!")
