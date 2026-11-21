"""
DSA - Strings 04: Z-Algorithm

Problem:
    Build the Z-array of a string: Z[i] is the length of the longest
    substring starting at i that is also a prefix of the string. Use it to
    find all occurrences of a pattern in a text.

Approach / Intuition:
    Maintain the "Z-box" [l, r): the rightmost window known to match the
    prefix. For i inside the box, s[i:r] mirrors s[i-l:r-l], so Z[i] is at
    least min(r - i, Z[i - l]) - reuse it instead of recomparing. Then try to
    extend past r character by character, and move the box if we do.
    Pattern search: compute Z on pattern + sep + text; positions where
    Z == len(pattern) are matches. The separator must not appear in either.

Complexity:
    Time:  O(n) - r only moves forward, so total extension work is linear
    Space: O(n) - the Z-array
"""

from typing import List


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    if n:
        z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def z_search(text: str, pattern: str, sep: str = "\x00") -> List[int]:
    if not pattern:
        return []
    combined = pattern + sep + text
    m = len(pattern)
    return [i - m - 1 for i, v in enumerate(z_array(combined)) if i > m and v >= m]


if __name__ == "__main__":
    assert z_array("aabxaab") == [7, 1, 0, 0, 3, 1, 0]
    assert z_array("aaaaa") == [5, 4, 3, 2, 1]
    assert z_array("") == []
    assert z_search("baabaa", "aab") == [1]
    assert z_search("aaaa", "aa") == [0, 1, 2]
    assert z_search("abcdef", "gh") == []
    print("All test cases passed!")
