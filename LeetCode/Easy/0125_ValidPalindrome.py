"""
LeetCode 125. Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/

Problem:
    A phrase is a palindrome if, after lowercasing and removing every
    non-alphanumeric character, it reads the same forward and backward.
    Given a string `s`, return True if it is a palindrome.

Approach / Intuition:
    Two pointers from both ends. Skip characters that are not alphanumeric,
    then compare the lowercase forms. Any mismatch means it is not a
    palindrome. This avoids building a cleaned copy of the string.

Complexity:
    Time:  O(n) - each character is looked at at most once
    Space: O(1) - only two indices
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("race a car") is False
    assert s.isPalindrome(" ") is True
    assert s.isPalindrome("0P") is False
    print("All test cases passed!")
