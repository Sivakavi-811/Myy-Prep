"""
LeetCode 387. First Unique Character in a String (Easy)
https://leetcode.com/problems/first-unique-character-in-a-string/

Problem:
    Return the index of the first non-repeating character in s, or -1.

Approach / Intuition:
    Two passes: count every character, then scan again in order and return
    the first index whose character has count 1.

Complexity:
    Time:  O(n)
    Space: O(1) - at most 26 lowercase letters counted
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.firstUniqChar("leetcode") == 0
    assert sol.firstUniqChar("loveleetcode") == 2
    assert sol.firstUniqChar("aabb") == -1
    assert sol.firstUniqChar("z") == 0
    print("All test cases passed!")
