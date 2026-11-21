"""
LeetCode 78. Subsets (Medium)
https://leetcode.com/problems/subsets/

Problem:
    Given an array of unique integers, return all possible subsets (the
    power set). The result must not contain duplicate subsets.

Approach / Intuition:
    Iterative "cascading": start with [[]]. For each number, every existing
    subset spawns a copy with that number added. After processing all n
    numbers there are 2^n subsets.
    (Equivalently, each subset corresponds to an n-bit mask indicating
    which elements are included.)

Complexity:
    Time:  O(n * 2^n) - 2^n subsets, up to n elements copied each
    Space: O(n * 2^n) - the output
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = [[]]
        for x in nums:
            result += [subset + [x] for subset in result]
        return result


if __name__ == "__main__":
    s = Solution()
    out = s.subsets([1, 2, 3])
    assert sorted(map(sorted, out)) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert s.subsets([0]) == [[], [0]]
    assert len(s.subsets(list(range(10)))) == 1024
    print("All test cases passed!")
