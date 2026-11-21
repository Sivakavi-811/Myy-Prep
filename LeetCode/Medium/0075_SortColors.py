"""
LeetCode 75. Sort Colors (Medium)
https://leetcode.com/problems/sort-colors/

Problem:
    Sort an array of 0s, 1s and 2s (red, white, blue) in place in a single
    pass, without a library sort.

Approach / Intuition:
    Dijkstra's Dutch National Flag partitioning with three pointers:
      [0, low)      -> 0s
      [low, mid)    -> 1s
      [mid, high]   -> unknown
      (high, end]   -> 2s
    Look at nums[mid]: a 0 swaps to `low` (both advance); a 1 just
    advances mid; a 2 swaps to `high` and high shrinks - but mid stays,
    because the value swapped in from high hasn't been examined yet.

Complexity:
    Time:  O(n) - one pass
    Space: O(1)
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    s = Solution()
    for given in ([2, 0, 2, 1, 1, 0], [2, 0, 1], [0], [1, 1], [2, 2, 0, 0], []):
        expected = sorted(given)
        s.sortColors(given)
        assert given == expected
    print("All test cases passed!")
