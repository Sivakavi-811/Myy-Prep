"""
LeetCode 198. House Robber (Medium)
https://leetcode.com/problems/house-robber/

Problem:
    Houses in a row hold given amounts of money. Robbing two adjacent houses
    triggers an alarm. Return the maximum amount you can rob.

Approach / Intuition:
    For each house, either skip it (keep the best up to the previous house)
    or rob it (its money + best up to two houses back):
        best[i] = max(best[i-1], best[i-2] + nums[i])
    Only the last two values are needed, so roll two variables.

Complexity:
    Time:  O(n) - single pass
    Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0  # best up to i-2, best up to i-1
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([2, 1, 1, 2]) == 4
    assert s.rob([5]) == 5
    assert s.rob([]) == 0
    print("All test cases passed!")
