"""
LeetCode 46. Permutations (Medium)
https://leetcode.com/problems/permutations/

Problem:
    Given an array of distinct integers, return all possible permutations.

Approach / Intuition:
    In-place swap backtracking. Positions [0, first) are already fixed.
    For position `first`, swap each remaining element (index >= first) into
    it, recurse to fix the next position, then swap back to restore the
    array. When first == n, the array is one full permutation.

Complexity:
    Time:  O(n * n!) - n! permutations, O(n) to copy each
    Space: O(n) - recursion depth (excluding output)
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        n = len(nums)

        def backtrack(first: int) -> None:
            if first == n:
                result.append(nums[:])
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return result


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(s.permute([0, 1])) == [[0, 1], [1, 0]]
    assert s.permute([1]) == [[1]]
    assert len(s.permute([1, 2, 3, 4, 5])) == 120
    print("All test cases passed!")
