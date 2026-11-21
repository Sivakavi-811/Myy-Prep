"""
LeetCode 228. Summary Ranges (Easy)
https://leetcode.com/problems/summary-ranges/

Problem:
    Given a sorted array of unique integers, return the smallest list of
    ranges covering all numbers exactly: "a->b" for a run, "a" for a single.

Approach / Intuition:
    Scan once, marking where each run of consecutive numbers starts. A run
    ends when the next number isn't current + 1 (or the array ends); emit
    it then and start a new run.

Complexity:
    Time:  O(n)
    Space: O(1) extra besides the output
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges: List[str] = []
        start = 0
        for i in range(len(nums)):
            if i + 1 == len(nums) or nums[i + 1] != nums[i] + 1:
                if start == i:
                    ranges.append(str(nums[i]))
                else:
                    ranges.append(f"{nums[start]}->{nums[i]}")
                start = i + 1
        return ranges


if __name__ == "__main__":
    s = Solution()
    assert s.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert s.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert s.summaryRanges([]) == []
    assert s.summaryRanges([-1]) == ["-1"]
    print("All test cases passed!")
