"""
DSA - Strings 03: Rabin-Karp Pattern Search (Rolling Hash)

Problem:
    Find every starting index where `pattern` occurs in `text`.

Approach / Intuition:
    Treat each length-m window of the text as a number in base B, modulo a
    large prime. Comparing hashes is O(1), and the next window's hash is
    derived from the current one in O(1) (a "rolling" hash):
        h' = (h - text[i] * B^(m-1)) * B + text[i + m]   (mod P)
    Different strings can share a hash (a collision), so every hash match
    is verified with a direct string comparison.

Complexity:
    Time:  O(n + m) expected; O(n * m) worst case with many collisions
    Space: O(1)
"""

from typing import List

BASE = 256
MOD = 1_000_000_007


def rabin_karp(text: str, pattern: str) -> List[int]:
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    high = pow(BASE, m - 1, MOD)
    p_hash = t_hash = 0
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD

    matches = []
    for i in range(n - m + 1):
        if t_hash == p_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * high) * BASE + ord(text[i + m])) % MOD
    return matches


if __name__ == "__main__":
    assert rabin_karp("GEEKS FOR GEEKS", "GEEK") == [0, 10]
    assert rabin_karp("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert rabin_karp("aaaa", "aa") == [0, 1, 2]
    assert rabin_karp("abc", "d") == []
    assert rabin_karp("ab", "abc") == []
    print("All test cases passed!")
