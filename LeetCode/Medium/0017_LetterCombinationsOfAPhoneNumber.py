"""
LeetCode 17. Letter Combinations of a Phone Number (Medium)
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Problem:
    Given a string of digits 2-9, return all letter combinations the number
    could represent on a phone keypad.

Approach / Intuition:
    Build combinations level by level: start with [""] and, for each digit,
    extend every partial combination with each of that digit's letters.
    This is the iterative form of backtracking over a fixed-depth tree.

Complexity:
    Time:  O(4^n * n) - up to 4 letters per digit, strings of length n
    Space: O(4^n * n) - the output
"""

from typing import List

KEYPAD = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos = [""]
        for d in digits:
            combos = [prefix + ch for prefix in combos for ch in KEYPAD[d]]
        return combos


if __name__ == "__main__":
    s = Solution()
    assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert s.letterCombinations("") == []
    assert s.letterCombinations("2") == ["a", "b", "c"]
    assert len(s.letterCombinations("79")) == 16
    print("All test cases passed!")
