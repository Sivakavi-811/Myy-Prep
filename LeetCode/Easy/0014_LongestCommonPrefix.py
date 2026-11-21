"""
LeetCode 14. Longest Common Prefix (Easy)
https://leetcode.com/problems/longest-common-prefix/

Problem:
    Return the longest common prefix shared by all strings in an array,
    or "" if there is none.

Approach / Intuition:
    Vertical scanning: compare characters column by column. The prefix
    ends at the first column where some string is too short or differs.
    zip(*strs) yields exactly these columns and stops at the shortest
    string automatically.

Complexity:
    Time:  O(S) - S = total characters examined (at most all of them)
    Space: O(1) extra besides the output
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for column in zip(*strs):
            if len(set(column)) != 1:
                break
            prefix.append(column[0])
        return "".join(prefix)


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["alone"]) == "alone"
    assert s.longestCommonPrefix(["", "b"]) == ""
    assert s.longestCommonPrefix(["ab", "abc", "abcd"]) == "ab"
    print("All test cases passed!")
