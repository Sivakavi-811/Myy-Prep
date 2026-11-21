"""
LeetCode 15. 3Sum (Medium)
https://leetcode.com/problems/3sum/

Problem:
    Given an integer array `nums`, return all unique triplets
    [a, b, c] with a + b + c == 0. The answer must not contain duplicates.

Approach / Intuition:
    Sort the array. Fix the first element nums[i], then find pairs summing
    to -nums[i] in the rest with two pointers (sorted => move left to grow
    the sum, right to shrink it).
    Skip equal values for i and after each found triplet to avoid
    duplicates. Stop early once nums[i] > 0 - no three non-negative
    sorted numbers can sum to 0 from there.

Complexity:
    Time:  O(n^2) - n choices for i, linear two-pointer scan each
    Space: O(1) extra (ignoring the output and the sort)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, result = len(nums), []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
        return result


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert sorted(s.threeSum([-2, 0, 0, 2, 2])) == [[-2, 0, 2]]
    print("All test cases passed!")
