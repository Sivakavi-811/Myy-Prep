"""
LeetCode 191. Number of 1 Bits (Easy)
https://leetcode.com/problems/number-of-1-bits/

Problem:
    Given a positive integer n, return the number of set bits (1s) in its
    binary representation (its Hamming weight).

Approach / Intuition:
    Brian Kernighan's trick: n & (n - 1) clears the lowest set bit
    (subtracting 1 flips that bit and every 0 below it). Repeat until n is
    0 - the loop runs once per set bit rather than once per bit position.

Complexity:
    Time:  O(k) - k = number of set bits (at most 32)
    Space: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.hammingWeight(11) == 3           # 1011
    assert s.hammingWeight(128) == 1          # 10000000
    assert s.hammingWeight(2147483645) == 30
    assert s.hammingWeight(0) == 0
    print("All test cases passed!")
