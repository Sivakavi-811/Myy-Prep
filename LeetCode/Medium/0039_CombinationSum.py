"""
LeetCode 39. Combination Sum (Medium)
https://leetcode.com/problems/combination-sum/

Problem:
    Given distinct positive integers `candidates` and a `target`, return all
    unique combinations whose sum is target. A number may be reused any
    number of times; combinations are unique as multisets.

Approach / Intuition:
    Backtracking over a sorted list. Each call picks a candidate at index
    >= start (so combinations are built in non-decreasing order and each
    multiset appears once). Passing `i` (not i + 1) to the recursive call
    allows reuse. Sorting lets us break as soon as a candidate exceeds the
    remaining target - every later one is larger still.

Complexity:
    Time:  O(N^(T/M + 1)) worst case - N candidates, T target, M min value
    Space: O(T/M) - recursion depth (excluding output)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break
                path.append(c)
                backtrack(i, remaining - c)
                path.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert s.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSum([2], 1) == []
    print("All test cases passed!")
