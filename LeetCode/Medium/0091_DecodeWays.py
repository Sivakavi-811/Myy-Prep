"""
LeetCode 91. Decode Ways (Medium)
https://leetcode.com/problems/decode-ways/

Problem:
    Letters map to numbers: A = 1, ..., Z = 26. Given a digit string,
    return how many ways it can be decoded. Codes like "06" are invalid.

Approach / Intuition:
    ways(i) = number of decodings of the prefix s[:i]. The last step uses
    either one digit or two:
      - one digit s[i-1] is valid if it isn't '0'  -> add ways(i - 1)
      - two digits s[i-2:i] are valid if in 10..26  -> add ways(i - 2)
    Like Fibonacci, only the previous two values are needed.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        prev2, prev1 = 0, 1  # ways(i-2), ways(i-1); ways(0) = 1
        for i in range(1, len(s) + 1):
            cur = 0
            if s[i - 1] != "0":
                cur += prev1
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                cur += prev2
            prev2, prev1 = prev1, cur
        return prev1


if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings("12") == 2      # AB, L
    assert sol.numDecodings("226") == 3     # BZ, VF, BBF
    assert sol.numDecodings("06") == 0
    assert sol.numDecodings("10") == 1
    assert sol.numDecodings("2101") == 1
    assert sol.numDecodings("11106") == 2
    print("All test cases passed!")
