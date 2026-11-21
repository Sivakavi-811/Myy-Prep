"""
LeetCode 70. Climbing Stairs (Easy)
https://leetcode.com/problems/climbing-stairs/

Problem:
    You are climbing a staircase with `n` steps. Each time you can climb 1 or
    2 steps. In how many distinct ways can you reach the top?

Approach / Intuition:
    The last move onto step n came from step n-1 or step n-2, so
        ways(n) = ways(n-1) + ways(n-2)
    which is the Fibonacci recurrence (ways(1) = 1, ways(2) = 2).
    Only the previous two values are needed, so keep two variables
    instead of a full DP table.

Complexity:
    Time:  O(n) - one loop up to n
    Space: O(1) - two rolling variables
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1  # ways(0), ways(1)
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(5) == 8
    assert s.climbStairs(45) == 1836311903
    print("All test cases passed!")
