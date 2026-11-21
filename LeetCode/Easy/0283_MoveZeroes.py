"""
LeetCode 283. Move Zeroes (Easy)
https://leetcode.com/problems/move-zeroes/

Problem:
    Move all 0s in `nums` to the end while keeping the relative order of the
    non-zero elements. Do it in place.

Approach / Intuition:
    Two pointers: `write` marks where the next non-zero belongs. Scan with
    `read`; whenever nums[read] is non-zero, swap it into position `write`
    and advance `write`. Swapping (rather than overwriting) pushes zeros
    toward the end automatically, so no second fill pass is needed.

Complexity:
    Time:  O(n) - single pass
    Space: O(1) - in place
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1


if __name__ == "__main__":
    s = Solution()
    for given, expected in [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1], [1, 0, 0]),
    ]:
        s.moveZeroes(given)
        assert given == expected
    print("All test cases passed!")
