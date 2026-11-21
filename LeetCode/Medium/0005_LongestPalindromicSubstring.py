"""
LeetCode 5. Longest Palindromic Substring (Medium)
https://leetcode.com/problems/longest-palindromic-substring/

Problem:
    Given a string `s`, return its longest palindromic substring.

Approach / Intuition:
    Expand around centers. Every palindrome mirrors around a center, which
    is either a character (odd length) or the gap between two characters
    (even length) - 2n - 1 centers in total. From each center, expand
    outward while both ends match, and track the longest span found.

Complexity:
    Time:  O(n^2) - each of the 2n-1 expansions is O(n) worst case
    Space: O(1)   - only indices are stored
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(lo: int, hi: int) -> tuple:
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return lo + 1, hi  # palindrome is s[lo+1:hi]

        best_lo, best_hi = 0, 0
        for i in range(len(s)):
            for lo, hi in (expand(i, i), expand(i, i + 1)):
                if hi - lo > best_hi - best_lo:
                    best_lo, best_hi = lo, hi
        return s[best_lo:best_hi]


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") in ("bab", "aba")
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("forgeeksskeegfor") == "geeksskeeg"
    print("All test cases passed!")
