"""
LeetCode 238. Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/

Problem:
    Given an integer array `nums`, return an array `answer` where answer[i]
    is the product of every element except nums[i]. Division is not allowed
    and the solution must run in O(n).

Approach / Intuition:
    answer[i] = (product of everything left of i) * (product of everything
    right of i). First pass fills `answer` with prefix products. Second pass
    walks from the right, carrying a running suffix product, and multiplies
    it in. The output array doubles as prefix storage, so no extra arrays.

Complexity:
    Time:  O(n) - two passes
    Space: O(1) - extra space besides the output array
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([2, 3]) == [3, 2]
    print("All test cases passed!")
