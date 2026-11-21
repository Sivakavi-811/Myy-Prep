"""
DSA - Strings 02: KMP Pattern Search

Problem:
    Find every starting index where `pattern` occurs in `text`.

Approach / Intuition:
    Naive search restarts after a mismatch and can take O(n * m).
    Knuth-Morris-Pratt precomputes the LPS array: lps[i] is the length of
    the longest proper prefix of pattern[0..i] that is also a suffix of it.
    On a mismatch after matching j characters, we already know the last
    lps[j-1] text characters equal the pattern's first lps[j-1] characters,
    so we continue from there instead of re-scanning. The text pointer
    never moves backward.

Complexity:
    Time:  O(n + m) - O(m) to build LPS, O(n) to scan the text
    Space: O(m)     - the LPS array
"""

from typing import List


def build_lps(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    for i in range(1, len(pattern)):
        while length and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length
    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    if not pattern:
        return []
    lps = build_lps(pattern)
    matches, j = [], 0
    for i, ch in enumerate(text):
        while j and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j - 1]
    return matches


if __name__ == "__main__":
    assert build_lps("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AAAAA", "AA") == [0, 1, 2, 3]
    assert kmp_search("hello", "xyz") == []
    assert kmp_search("abc", "") == []
    print("All test cases passed!")
