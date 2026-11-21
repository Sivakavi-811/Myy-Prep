"""
LeetCode 84. Largest Rectangle in Histogram (Hard)
https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem:
    Given bar heights of a histogram (each bar width 1), return the area of
    the largest rectangle that fits inside it.

Approach / Intuition:
    For each bar, the best rectangle using its full height extends left
    and right until a shorter bar. A monotonic increasing stack of indices
    finds both limits in one pass: when bar i is shorter than the bar on
    top of the stack, that top bar can't extend past i (right limit), and
    the new top below it is its left limit. Pop and compute its area.
    A sentinel height 0 at the end flushes the remaining bars.

Complexity:
    Time:  O(n) - each index pushed and popped once
    Space: O(n) - the stack
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[int] = []  # indices with increasing heights
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                best = max(best, height * (i - left))
            stack.append(i)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([1, 1, 1, 1]) == 4
    assert s.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12
    assert s.largestRectangleArea([]) == 0
    print("All test cases passed!")
