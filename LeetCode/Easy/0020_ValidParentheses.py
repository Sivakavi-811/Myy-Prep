"""
LeetCode 20. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Problem:
    Given a string containing only '(', ')', '{', '}', '[' and ']', decide
    whether it is valid: every opening bracket is closed by the same type of
    bracket, and brackets close in the correct order.

Approach / Intuition:
    The most recently opened bracket must be the first one closed, which is
    exactly Last-In-First-Out behaviour, so use a stack.
      - Push every opening bracket.
      - On a closing bracket, the stack top must be its matching opener;
        otherwise the string is invalid.
    At the end the stack must be empty (no unclosed openers).
    Quick win: an odd-length string can never be valid.

Complexity:
    Time:  O(n)  - each character is pushed/popped at most once
    Space: O(n)  - the stack holds up to n characters in the worst case
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("{[]}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("((") is False
    assert s.isValid("]") is False
    print("All test cases passed!")
