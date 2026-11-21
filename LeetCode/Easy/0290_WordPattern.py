"""
LeetCode 290. Word Pattern (Easy)
https://leetcode.com/problems/word-pattern/

Problem:
    Given a pattern (e.g. "abba") and a string of space-separated words,
    return True if the words follow the pattern via a bijection between
    pattern letters and words.

Approach / Intuition:
    Same idea as Isomorphic Strings, but at word level. Check the counts
    match first, then maintain letter -> word and word -> letter maps; any
    conflict in either direction breaks the bijection.

Complexity:
    Time:  O(n + m) - pattern length + total characters in s
    Space: O(n + m) - the maps and split words
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        p_to_w, w_to_p = {}, {}
        for ch, word in zip(pattern, words):
            if p_to_w.setdefault(ch, word) != word or w_to_p.setdefault(word, ch) != ch:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordPattern("abba", "dog cat cat dog") is True
    assert sol.wordPattern("abba", "dog cat cat fish") is False
    assert sol.wordPattern("aaaa", "dog cat cat dog") is False
    assert sol.wordPattern("abba", "dog dog dog dog") is False
    assert sol.wordPattern("aaa", "aa aa aa aa") is False
    print("All test cases passed!")
