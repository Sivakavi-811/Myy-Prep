"""
LeetCode 171. Excel Sheet Column Number (Easy)
https://leetcode.com/problems/excel-sheet-column-number/

Problem:
    Convert an Excel column title ("A", "Z", "AA", "ZY", ...) to its column
    number (A = 1, Z = 26, AA = 27, ...).

Approach / Intuition:
    It's base-26 with digits 1..26 instead of 0..25 (no zero digit).
    Horner's method: result = result * 26 + value(ch) for each character,
    left to right.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord("A") + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.titleToNumber("A") == 1
    assert s.titleToNumber("Z") == 26
    assert s.titleToNumber("AB") == 28
    assert s.titleToNumber("ZY") == 701
    assert s.titleToNumber("FXSHRXW") == 2147483647
    print("All test cases passed!")
