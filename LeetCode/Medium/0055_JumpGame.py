"""
LeetCode 55. Jump Game (Medium)
https://leetcode.com/problems/jump-game/

Problem:
    You start at index 0. nums[i] is the maximum jump length from index i.
    Return True if you can reach the last index.

Approach / Intuition:
    Greedy: track `reach`, the farthest index reachable so far. Scan left
    to right; if the current index is beyond `reach`, we're stuck. Otherwise
    extend reach with i + nums[i]. Once reach covers the last index, succeed.

Complexity:
    Time:  O(n) - single pass
    Space: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
            if reach >= len(nums) - 1:
                return True
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
    assert s.canJump([0]) is True
    assert s.canJump([0, 1]) is False
    assert s.canJump([2, 0, 0]) is True
    print("All test cases passed!")
