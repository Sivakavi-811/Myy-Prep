"""
LeetCode 344. Reverse String (Easy)
https://leetcode.com/problems/reverse-string/

Problem:
    Reverse an array of characters in place with O(1) extra memory.

Approach / Intuition:
    Two pointers at the ends; swap and move inward until they meet.

Complexity:
    Time:  O(n) - n/2 swaps
    Space: O(1)
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    sol = Solution()
    for given, expected in [
        (list("hello"), list("olleh")),
        (list("Hannah"), list("hannaH")),
        (["a"], ["a"]),
        (list("ab"), list("ba")),
    ]:
        sol.reverseString(given)
        assert given == expected
    print("All test cases passed!")
