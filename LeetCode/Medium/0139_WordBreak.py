"""
LeetCode 139. Word Break (Medium)
https://leetcode.com/problems/word-break/

Problem:
    Given a string s and a dictionary of words, return True if s can be
    split into a sequence of one or more dictionary words (words may be
    reused).

Approach / Intuition:
    dp[i] = True if the prefix s[:i] can be segmented. dp[0] = True (empty).
    For each end i, look back only as far as the longest dictionary word:
    if some dp[j] is True and s[j:i] is a word, then dp[i] is True.
    Bounding the look-back by the max word length keeps the inner loop small.

Complexity:
    Time:  O(n * L) substring checks - L = max word length (each O(L) to hash)
    Space: O(n + total dictionary size)
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        max_len = max(map(len, words), default=0)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert sol.wordBreak("a", []) is False
    print("All test cases passed!")
