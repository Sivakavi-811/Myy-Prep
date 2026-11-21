"""
LeetCode 13. Roman to Integer (Easy)
https://leetcode.com/problems/roman-to-integer/

Problem:
    Convert a Roman numeral string (I, V, X, L, C, D, M) to an integer.
    Subtractive pairs such as IV (4) and CM (900) must be handled.

Approach / Intuition:
    Read left to right. A symbol smaller than the one after it is
    subtracted (the I in IV); otherwise it is added. Comparing each symbol
    with its right neighbour handles all six subtractive cases uniformly.

Complexity:
    Time:  O(n) - one pass
    Space: O(1) - fixed 7-entry lookup table
"""

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s):
            v = VALUES[ch]
            if i + 1 < len(s) and v < VALUES[s[i + 1]]:
                total -= v
            else:
                total += v
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("MMMCMXCIX") == 3999
    print("All test cases passed!")
