"""
LeetCode 3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
    Given a string `s`, find the length of the longest substring that
    contains no repeated characters.

Approach / Intuition:
    Sliding window [left, right]. Remember the last index where each
    character was seen. When s[right] was already seen inside the current
    window, jump `left` to just past that previous occurrence - the window
    stays duplicate-free without shrinking one step at a time.

Complexity:
    Time:  O(n) - each index is processed once
    Space: O(min(n, alphabet)) - the last-seen map
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = best = 0
        for right, ch in enumerate(s):
            if last_seen.get(ch, -1) >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("abba") == 2
    print("All test cases passed!")
