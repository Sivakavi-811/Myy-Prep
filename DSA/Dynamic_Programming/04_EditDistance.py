"""
DSA - Dynamic Programming 04: Edit Distance (Levenshtein Distance)

Problem:
    Given two words a and b, return the minimum number of single-character
    insertions, deletions or substitutions needed to turn a into b.

Approach / Intuition:
    dp[i][j] = edit distance between a[:i] and b[:j].
      - Base cases: dp[i][0] = i (delete all), dp[0][j] = j (insert all).
      - If a[i-1] == b[j-1], no operation is needed: dp[i-1][j-1].
      - Else 1 + min of:
            dp[i-1][j]    delete a[i-1]
            dp[i][j-1]    insert b[j-1]
            dp[i-1][j-1]  substitute
    Each row depends only on the previous row, so keep one row plus the
    saved diagonal value.

Complexity:
    Time:  O(m * n)
    Space: O(n) - single rolling row
"""


def edit_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    row = list(range(n + 1))
    for i in range(1, m + 1):
        diag, row[0] = row[0], i
        for j in range(1, n + 1):
            above = row[j]
            if a[i - 1] == b[j - 1]:
                row[j] = diag
            else:
                row[j] = 1 + min(above, row[j - 1], diag)
            diag = above
    return row[n]


if __name__ == "__main__":
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "") == 3
    assert edit_distance("same", "same") == 0
    print("All test cases passed!")
