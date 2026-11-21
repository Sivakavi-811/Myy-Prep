"""
LeetCode 69. Sqrt(x) (Easy)
https://leetcode.com/problems/sqrtx/

Problem:
    Given a non-negative integer x, return floor(sqrt(x)) without using any
    built-in exponent or square-root function.

Approach / Intuition:
    Binary search for the largest k with k * k <= x. The predicate
    "k * k <= x" is true for small k and false beyond the answer, so it is
    monotonic. Search on [0, x // 2 + 1] (for x >= 2, sqrt(x) <= x / 2) and
    use an upper-biased mid so lo = mid always makes progress.

Complexity:
    Time:  O(log x)
    Space: O(1)
"""

from math import isqrt


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x // 2 + 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid <= x:
                lo = mid
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    for x in list(range(200)) + [2**31 - 1]:
        assert s.mySqrt(x) == isqrt(x)
    print("All test cases passed!")
