"""
LeetCode 438. Find All Anagrams in a String (Medium)
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Problem:
    Given strings s and p, return the start indices of every substring of
    s that is an anagram of p.

Approach / Intuition:
    Fixed-size sliding window of length len(p) with 26-letter counts.
    Instead of comparing whole count arrays each step, track `matches`:
    how many of the 26 letters currently have equal counts in the window
    and in p. Adding or removing a letter changes at most that letter's
    match status, so each slide is O(1). A window is an anagram when all
    26 letters match.

Complexity:
    Time:  O(n)
    Space: O(1) - two arrays of 26
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        need, have = [0] * 26, [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1

        matches = sum(1 for i in range(26) if need[i] == have[i])
        result: List[int] = []

        def update(idx: int, delta: int) -> None:
            nonlocal matches
            if have[idx] == need[idx]:
                matches -= 1
            have[idx] += delta
            if have[idx] == need[idx]:
                matches += 1

        for i, ch in enumerate(s):
            update(ord(ch) - 97, 1)
            if i >= m:
                update(ord(s[i - m]) - 97, -1)
            if matches == 26:
                result.append(i - m + 1)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
    assert sol.findAnagrams("a", "ab") == []
    assert sol.findAnagrams("aaaa", "aa") == [0, 1, 2]
    print("All test cases passed!")
