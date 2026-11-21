"""
LeetCode 152. Maximum Product Subarray (Medium)
https://leetcode.com/problems/maximum-product-subarray/

Problem:
    Given an integer array, find the contiguous subarray with the largest
    product and return that product.

Approach / Intuition:
    Like Kadane's, but a negative number flips the biggest product into the
    smallest and vice versa. So track both the max and min product of a
    subarray ending at the current index. For each x, the new max/min come
    from {x, x * old_max, x * old_min}. A zero naturally resets both to 0,
    and the next element restarts the run.

Complexity:
    Time:  O(n) - single pass
    Space: O(1)
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = best = nums[0]
        for x in nums[1:]:
            candidates = (x, x * cur_max, x * cur_min)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
    assert s.maxProduct([-2]) == -2
    print("All test cases passed!")
