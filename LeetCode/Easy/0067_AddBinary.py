"""
LeetCode 67. Add Binary (Easy)
https://leetcode.com/problems/add-binary/

Problem:
    Given two binary strings a and b, return their sum as a binary string.

Approach / Intuition:
    Grade-school addition from the rightmost bits with a carry. At each step
    total = bit_a + bit_b + carry; output total % 2 and carry total // 2.
    Continue while either string has bits left or a carry remains, then
    reverse the collected bits.

Complexity:
    Time:  O(max(m, n))
    Space: O(max(m, n)) - the result
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        bits = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += a[i] == "1"
                i -= 1
            if j >= 0:
                total += b[j] == "1"
                j -= 1
            bits.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(bits))


if __name__ == "__main__":
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("1111", "1") == "10000"
    print("All test cases passed!")
