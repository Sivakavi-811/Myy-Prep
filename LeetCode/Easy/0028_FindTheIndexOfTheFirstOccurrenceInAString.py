"""
LeetCode 28. Find the Index of the First Occurrence in a String (Easy)
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Problem:
    Return the index of the first occurrence of `needle` in `haystack`, or
    -1 if needle is not part of haystack.

Approach / Intuition:
    KMP for guaranteed linear time. Build the LPS (longest proper prefix
    that is also a suffix) table for the needle, then scan the haystack
    once; on a mismatch, fall back via LPS instead of moving the haystack
    pointer backward. Return as soon as the whole needle matches.

Complexity:
    Time:  O(n + m)
    Space: O(m) - the LPS table
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        lps = [0] * len(needle)
        k = 0
        for i in range(1, len(needle)):
            while k and needle[i] != needle[k]:
                k = lps[k - 1]
            if needle[i] == needle[k]:
                k += 1
            lps[i] = k

        j = 0
        for i, ch in enumerate(haystack):
            while j and ch != needle[j]:
                j = lps[j - 1]
            if ch == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1
    assert s.strStr("mississippi", "issip") == 4
    assert s.strStr("aaaaab", "aab") == 3
    assert s.strStr("a", "a") == 0
    print("All test cases passed!")
