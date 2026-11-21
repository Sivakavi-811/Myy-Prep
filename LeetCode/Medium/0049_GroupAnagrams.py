"""
LeetCode 49. Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/

Problem:
    Given an array of strings `strs`, group the anagrams together. The
    answer may be returned in any order.

Approach / Intuition:
    Anagrams share the same letter counts. Build a key from the 26-letter
    frequency tuple of each word and bucket words by that key in a hash map.
    A counting key costs O(k) per word, versus O(k log k) for a sorted-string
    key.

Complexity:
    Time:  O(n * k) - n words, k = max word length
    Space: O(n * k) - the map stores every word plus its key
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())


def normalize(groups: List[List[str]]) -> List[List[str]]:
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    s = Solution()
    assert normalize(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    print("All test cases passed!")
