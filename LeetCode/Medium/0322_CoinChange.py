"""
LeetCode 322. Coin Change (Medium)
https://leetcode.com/problems/coin-change/

Problem:
    Given coin denominations and a target `amount`, return the fewest coins
    needed to make that amount, or -1 if it can't be made. Each coin may be
    used any number of times.

Approach / Intuition:
    Bottom-up DP (unbounded knapsack). dp[a] = fewest coins to make a.
    dp[0] = 0; for each amount a, try every coin c <= a as the last coin:
        dp[a] = min(dp[a], dp[a - c] + 1)
    Greedy (largest coin first) fails, e.g. coins [1, 3, 4], amount 6:
    greedy gives 4+1+1 (3 coins) but 3+3 needs only 2.

Complexity:
    Time:  O(amount * len(coins))
    Space: O(amount)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [0] + [INF] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1
        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([1, 3, 4], 6) == 2
    print("All test cases passed!")
