"""
LeetCode 9. Palindrome Number (Easy)
https://leetcode.com/problems/palindrome-number/

Problem:
    Given an integer x, return True if x reads the same forward and
    backward, without converting it to a string.

Approach / Intuition:
    Negative numbers and numbers ending in 0 (except 0 itself) can't be
    palindromes. Otherwise reverse only the second half of the digits:
    pop digits off x onto `rev` until rev >= x. Then x == rev (even length)
    or x == rev // 10 (odd length - the middle digit sits in rev).
    Reversing half avoids overflow in fixed-width languages.

Complexity:
    Time:  O(log10 n) - half the digits are processed
    Space: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(0) is True
    assert s.isPalindrome(1221) is True
    assert s.isPalindrome(12321) is True
    print("All test cases passed!")
