"""
LeetCode 150. Evaluate Reverse Polish Notation (Medium)
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Problem:
    Evaluate an arithmetic expression given in Reverse Polish (postfix)
    notation. Operators are + - * /, and division truncates toward zero.

Approach / Intuition:
    Use a stack. Push numbers; on an operator, pop the right operand first,
    then the left, apply the operator, and push the result. A valid
    expression leaves exactly one value.
    Note: Python's // floors (rounds toward -inf), so use int(a / b) to
    truncate toward zero as required (e.g. -7 / 2 -> -3, not -4).

Complexity:
    Time:  O(n) - each token processed once
    Space: O(n) - the stack
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for tok in tokens:
            if tok in {"+", "-", "*", "/"}:
                b, a = stack.pop(), stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(tok))
        return stack[0]


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert s.evalRPN(["-7", "2", "/"]) == -3
    print("All test cases passed!")
