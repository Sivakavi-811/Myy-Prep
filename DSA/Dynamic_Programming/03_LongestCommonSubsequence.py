"""
DSA - Dynamic Programming 03: Longest Common Subsequence (LCS)

Problem:
    Given two strings, find the length of their longest common subsequence
    (characters in the same relative order, not necessarily contiguous),
    and reconstruct one such subsequence.

Approach / Intuition:
    dp[i][j] = LCS length of a[:i] and b[:j].
      - If a[i-1] == b[j-1], that character extends the LCS:
            dp[i][j] = dp[i-1][j-1] + 1
      - Otherwise drop one character from either string:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    To reconstruct, walk back from dp[m][n]: on a match take the character
    and move diagonally; otherwise step toward the larger neighbour.

Complexity:
    Time:  O(m * n)
    Space: O(m * n) for the table (length-only can be done in O(min(m, n)))
"""

from typing import List, Tuple


def lcs(a: str, b: str) -> Tuple[int, str]:
    m, n = len(a), len(b)
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    chars: List[str] = []
    i, j = m, n
    while i and j:
        if a[i - 1] == b[j - 1]:
            chars.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], "".join(reversed(chars))


def is_subsequence(sub: str, s: str) -> bool:
    it = iter(s)
    return all(ch in it for ch in sub)


if __name__ == "__main__":
    length, seq = lcs("ABCBDAB", "BDCABA")
    assert length == 4 and len(seq) == 4
    assert is_subsequence(seq, "ABCBDAB") and is_subsequence(seq, "BDCABA")

    assert lcs("abcde", "ace") == (3, "ace")
    assert lcs("abc", "def") == (0, "")
    assert lcs("", "abc") == (0, "")
    print("All test cases passed!")
