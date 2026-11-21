"""
LeetCode 242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Problem:
    Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
    i.e. it uses exactly the same characters with the same frequencies.

Approach / Intuition:
    Two strings are anagrams exactly when their character counts match.
      1. If the lengths differ, they cannot be anagrams.
      2. Count characters of s (+1) and t (-1) in one frequency array.
      3. Every count must end at 0.
    The input is lowercase English letters, so a fixed 26-slot array works.
    (Follow-up for Unicode input: use a hash map / collections.Counter.)

Complexity:
    Time:  O(n)  - one pass over both strings
    Space: O(1)  - fixed array of 26 counters (O(k) for a k-letter alphabet)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for a, b in zip(s, t):
            counts[ord(a) - ord("a")] += 1
            counts[ord(b) - ord("a")] -= 1
        return all(c == 0 for c in counts)


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    assert s.isAnagram("a", "ab") is False
    assert s.isAnagram("listen", "silent") is True
    print("All test cases passed!")
