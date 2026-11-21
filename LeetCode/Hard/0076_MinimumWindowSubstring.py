"""
LeetCode 76. Minimum Window Substring (Hard)
https://leetcode.com/problems/minimum-window-substring/

Problem:
    Given strings s and t, return the shortest substring of s that contains
    every character of t (including duplicates), or "" if none exists.

Approach / Intuition:
    Sliding window with a "missing" counter. `need` holds how many of each
    character the window still lacks; `missing` is the total still lacking.
      - Expand right: if s[right] was still needed, missing decreases.
      - Once missing == 0 the window is valid: shrink from the left past
        characters that aren't required (need < 0 means a surplus),
        record the window, then drop one required char to search again.
    Every index enters and leaves the window at most once.

Complexity:
    Time:  O(|s| + |t|)
    Space: O(k) - k = distinct characters in t
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        best_lo, best_hi = 0, 0  # empty window = not found
        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if best_hi == 0 or right - left < best_hi - best_lo:
                    best_lo, best_hi = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[best_lo:best_hi]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow("aa", "aa") == "aa"
    assert sol.minWindow("bba", "ab") == "ba"
    print("All test cases passed!")
