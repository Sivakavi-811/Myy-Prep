"""
LeetCode 121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
    `prices[i]` is the price of a stock on day i. Choose one day to buy and a
    later day to sell to maximise profit. Return the maximum profit, or 0 if
    no profitable transaction exists.

Approach / Intuition:
    If we sell on day i, the best buy day is the cheapest day before i.
    So scan once, tracking:
      - min_price: the lowest price seen so far (best buy point)
      - best:      the best profit from selling today at prices[i]
    Each day, update best with (price - min_price), then update min_price.
    This is a one-pass greedy / running-minimum technique.

Complexity:
    Time:  O(n)  - single pass over prices
    Space: O(1)  - two variables
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best:
                best = price - min_price
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([2, 4, 1]) == 2
    assert s.maxProfit([1]) == 0
    print("All test cases passed!")
