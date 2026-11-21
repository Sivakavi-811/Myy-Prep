"""
LeetCode 383. Ransom Note (Easy)
https://leetcode.com/problems/ransom-note/

Problem:
    Return True if `ransomNote` can be built from the letters of `magazine`,
    using each magazine letter at most once.

Approach / Intuition:
    Count the magazine's letters, then spend them on the note. If any
    letter's count drops below zero, the magazine doesn't have enough.
    Exiting on the first shortfall avoids a full second comparison.

Complexity:
    Time:  O(m + n)
    Space: O(1) - at most 26 lowercase letters tracked
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        available = Counter(magazine)
        for ch in ransomNote:
            available[ch] -= 1
            if available[ch] < 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canConstruct("a", "b") is False
    assert s.canConstruct("aa", "ab") is False
    assert s.canConstruct("aa", "aab") is True
    assert s.canConstruct("", "abc") is True
    print("All test cases passed!")
