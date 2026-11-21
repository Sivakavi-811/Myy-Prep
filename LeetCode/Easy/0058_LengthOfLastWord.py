"""
LeetCode 58. Length of Last Word (Easy)
https://leetcode.com/problems/length-of-last-word/

Problem:
    Given a string of words and spaces, return the length of the last word.
    A word is a maximal run of non-space characters.

Approach / Intuition:
    Scan from the end: skip trailing spaces, then count characters until
    the next space or the start of the string. Only the tail of the string
    is touched, with no split() allocation.

Complexity:
    Time:  O(n) worst case, usually much less
    Space: O(1)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
    assert s.lengthOfLastWord("a") == 1
    print("All test cases passed!")
