"""
LeetCode 155. Min Stack (Medium)
https://leetcode.com/problems/min-stack/

Problem:
    Design a stack that supports push, pop, top and getMin, each in O(1).

Approach / Intuition:
    Store pairs (value, min_so_far) on a single stack. When pushing, the
    new minimum is min(value, current minimum). Because each entry
    remembers the minimum at the time it was pushed, popping automatically
    restores the previous minimum - nothing has to be recomputed.

Complexity:
    Time:  O(1) for every operation
    Space: O(n) - one pair per element
"""


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2

    ms = MinStack()
    for v in (5, 5, 3, 3):
        ms.push(v)
    ms.pop()
    assert ms.getMin() == 3
    ms.pop()
    assert ms.getMin() == 5
    print("All test cases passed!")
