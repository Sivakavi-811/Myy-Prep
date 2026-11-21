"""
LeetCode 739. Daily Temperatures (Medium)
https://leetcode.com/problems/daily-temperatures/

Problem:
    Given daily temperatures, return for each day how many days you must
    wait for a warmer temperature (0 if no warmer day comes).

Approach / Intuition:
    Monotonic decreasing stack of indices still waiting for a warmer day.
    For each day i, pop every waiting day whose temperature is lower - day
    i is their answer, and the wait is i - j. Then push i to wait itself.

Complexity:
    Time:  O(n) - each index pushed and popped once
    Space: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack: List[int] = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert s.dailyTemperatures([50, 50, 50]) == [0, 0, 0]
    print("All test cases passed!")
