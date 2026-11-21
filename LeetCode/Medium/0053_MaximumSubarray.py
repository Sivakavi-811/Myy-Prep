"""
LeetCode 53. Maximum Subarray (Medium)
https://leetcode.com/problems/maximum-subarray/

Problem:
    Given an integer array `nums`, find the contiguous subarray (containing at
    least one number) with the largest sum and return that sum.

Approach / Intuition:
    Kadane's algorithm. Walk the array keeping `cur`, the best sum of a
    subarray that ends at the current index. At each element we either extend
    the previous subarray or start fresh here - whichever is larger:
        cur = max(x, cur + x)
    A negative running sum can only hurt what follows, so it is dropped.
    The answer is the maximum `cur` seen anywhere.

Complexity:
    Time:  O(n) - single pass
    Space: O(1) - two running variables
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([-3, -1, -2]) == -1
    print("All test cases passed!")
