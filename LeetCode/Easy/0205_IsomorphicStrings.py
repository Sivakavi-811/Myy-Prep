"""
LeetCode 205. Isomorphic Strings (Easy)
https://leetcode.com/problems/isomorphic-strings/

Problem:
    Two strings s and t are isomorphic if s's characters can be replaced
    to get t, where every occurrence of a character maps to the same
    character, and no two characters map to the same character.

Approach / Intuition:
    The mapping must be a bijection, so keep two maps (s -> t and t -> s).
    For each aligned pair, if either side already has a different partner,
    the strings aren't isomorphic. A single map would miss cases like
    "ab" -> "aa" (both a and b mapping to a).

Complexity:
    Time:  O(n)
    Space: O(k) - k = size of the character set
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for a, b in zip(s, t):
            if s_to_t.setdefault(a, b) != b or t_to_s.setdefault(b, a) != a:
                return False
        return len(s) == len(t)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("egg", "add") is True
    assert sol.isIsomorphic("foo", "bar") is False
    assert sol.isIsomorphic("paper", "title") is True
    assert sol.isIsomorphic("badc", "baba") is False
    assert sol.isIsomorphic("ab", "aa") is False
    print("All test cases passed!")
