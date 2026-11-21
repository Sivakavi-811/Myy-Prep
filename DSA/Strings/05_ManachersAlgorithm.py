"""
DSA - Strings 05: Manacher's Algorithm (Longest Palindromic Substring in O(n))

Problem:
    Find the longest palindromic substring of a string in linear time.

Approach / Intuition:
    1. Insert a separator between characters ("aba" -> "^#a#b#a#$") so odd
       and even palindromes are handled the same way (all centered on a
       character). The ^ and $ sentinels stop expansion without bounds checks.
    2. p[i] = radius of the palindrome centered at i in the transformed
       string (which equals its length in the original string).
    3. Track the palindrome reaching farthest right: (center, right).
       For i < right, its mirror 2*center - i gives a free lower bound:
           p[i] >= min(right - i, p[mirror])
       Then expand normally. `right` only moves forward, so the total
       expansion work is O(n).

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from typing import List


def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    t = "^#" + "#".join(s) + "#$"
    p: List[int] = [0] * len(t)
    center = right = 0
    for i in range(1, len(t) - 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]

    length, idx = max((v, i) for i, v in enumerate(p))
    start = (idx - length) // 2
    return s[start:start + length]


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abacdfgdcaba") in ("aba", "aca")
    print("All test cases passed!")
