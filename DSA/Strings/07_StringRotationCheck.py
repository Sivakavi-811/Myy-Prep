"""
DSA - Strings 07: Check if One String Is a Rotation of Another

Problem:
    Given strings a and b, decide whether b can be obtained by rotating a
    (moving some prefix of a to its end). E.g. "waterbottle" ->
    "erbottlewat" is a rotation. Also find the lexicographically smallest
    rotation of a string.

Approach / Intuition:
    Every rotation of a appears as a substring of a + a (the doubled string
    contains all n cyclic shifts). So b is a rotation of a exactly when
    len(a) == len(b) and b occurs in a + a. Using KMP for the substring test
    keeps it linear.
    Smallest rotation: Booth's-style two-candidate comparison over a + a -
    compare rotations starting at i and j; on a mismatch at offset k, the
    loser's starts i..i+k can all be skipped.

Complexity:
    Rotation check:    O(n) time, O(n) space
    Smallest rotation: O(n) time, O(n) space
"""


def kmp_contains(text: str, pattern: str) -> bool:
    if not pattern:
        return True
    lps = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]:
            k = lps[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        lps[i] = k
    j = 0
    for ch in text:
        while j and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                return True
    return False


def is_rotation(a: str, b: str) -> bool:
    return len(a) == len(b) and kmp_contains(a + a, b)


def smallest_rotation(s: str) -> str:
    n = len(s)
    if n == 0:
        return s
    t = s + s
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        if t[i + k] == t[j + k]:
            k += 1
            continue
        if t[i + k] > t[j + k]:
            i += k + 1
        else:
            j += k + 1
        if i == j:
            j += 1
        k = 0
    start = min(i, j)
    return t[start:start + n]


if __name__ == "__main__":
    assert is_rotation("waterbottle", "erbottlewat") is True
    assert is_rotation("abcd", "cdab") is True
    assert is_rotation("abcd", "acbd") is False
    assert is_rotation("aa", "aaa") is False
    assert is_rotation("", "") is True

    for s in ("bca", "cbaab", "aaaa", "dcba", "abab", "z"):
        assert smallest_rotation(s) == min(s[i:] + s[:i] for i in range(len(s)))
    print("All test cases passed!")
