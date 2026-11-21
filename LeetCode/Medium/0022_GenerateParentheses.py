"""
LeetCode 22. Generate Parentheses (Medium)
https://leetcode.com/problems/generate-parentheses/

Problem:
    Given n pairs of parentheses, generate all combinations of
    well-formed parentheses.

Approach / Intuition:
    Backtracking that only ever builds valid prefixes:
      - add "(" while fewer than n opens have been used;
      - add ")" only while closes < opens (so it always has a match).
    When the string reaches length 2n it is guaranteed to be valid, so no
    filtering is needed afterwards.

Complexity:
    Time:  O(4^n / sqrt(n)) - the n-th Catalan number of results, each O(n)
    Space: O(n) - recursion depth and the current path (excluding output)
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []
        path: List[str] = []

        def backtrack(opens: int, closes: int) -> None:
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            if opens < n:
                path.append("(")
                backtrack(opens + 1, closes)
                path.pop()
            if closes < opens:
                path.append(")")
                backtrack(opens, closes + 1)
                path.pop()

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert s.generateParenthesis(1) == ["()"]
    assert len(s.generateParenthesis(4)) == 14  # Catalan(4)
    print("All test cases passed!")
