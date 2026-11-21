"""
LeetCode 66. Plus One (Easy)
https://leetcode.com/problems/plus-one/

Problem:
    A large integer is given as an array of digits (most significant
    first). Add one to it and return the resulting digit array.

Approach / Intuition:
    Walk from the last digit. A digit below 9 simply increments and we're
    done - no carry. A 9 becomes 0 and the carry moves left. If every digit
    was 9 (e.g. 999), the result is 1 followed by all zeros.

Complexity:
    Time:  O(n) worst case (all 9s), O(1) typical
    Space: O(1) extra, O(n) only for the all-9s case
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plusOne([1, 9]) == [2, 0]
    print("All test cases passed!")
