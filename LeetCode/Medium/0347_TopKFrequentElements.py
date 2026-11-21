"""
LeetCode 347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Problem:
    Given an integer array `nums` and an integer `k`, return the k most
    frequent elements, in any order. Must beat O(n log n).

Approach / Intuition:
    Bucket sort by frequency. Count each value, then place values into
    buckets indexed by their count (a count can be at most n). Walk the
    buckets from highest frequency down and collect values until we have k.
    This avoids sorting entirely.

Complexity:
    Time:  O(n) - counting + bucket fill + bucket scan
    Space: O(n) - the counter and buckets
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for value, freq in Counter(nums).items():
            buckets[freq].append(value)
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for value in buckets[freq]:
                result.append(value)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert sorted(s.topKFrequent([4, 4, 5, 5, 5, 6], 1)) == [5]
    print("All test cases passed!")
