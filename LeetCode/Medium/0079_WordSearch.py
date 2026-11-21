"""
LeetCode 79. Word Search (Medium)
https://leetcode.com/problems/word-search/

Problem:
    Given an m x n grid of letters and a word, return True if the word can
    be formed from sequentially adjacent cells (horizontal/vertical), with
    no cell used more than once.

Approach / Intuition:
    DFS backtracking from every cell matching word[0]. Temporarily mark the
    current cell as used (overwrite with '#') so the path can't revisit it,
    explore the four neighbours for the next character, then restore it.
    Quick prune: if the board lacks enough of some letter, return early.

Complexity:
    Time:  O(m * n * 3^L) - L = word length; each step has <= 3 new directions
    Space: O(L) - recursion depth
"""

from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        have = Counter(ch for row in board for ch in row)
        if any(have[ch] < cnt for ch, cnt in Counter(word).items()):
            return False

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[k]:
                return False
            board[r][c] = "#"
            found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1)
                     or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
            board[r][c] = word[k]
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert s.exist(board, "ABCCED") is True
    assert s.exist(board, "SEE") is True
    assert s.exist(board, "ABCB") is False  # would reuse B
    assert s.exist([["a"]], "a") is True
    print("All test cases passed!")
