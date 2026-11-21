"""
LeetCode 215. Kth Largest Element in an Array (Medium)
https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem:
    Return the k-th largest element in an unsorted array (by sorted order,
    not distinct values).

Approach / Intuition:
    Keep a min-heap of size k holding the k largest values seen so far.
    For each new value, push it; if the heap grows past k, pop the smallest.
    After the scan, the heap's root is the k-th largest overall.
    (Quickselect achieves O(n) average but O(n^2) worst case; the heap is
    predictable and memory is only O(k).)

Complexity:
    Time:  O(n log k)
    Space: O(k)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap[0]


if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([1], 1) == 1
    assert s.findKthLargest([-1, -2, -3], 3) == -3
    print("All test cases passed!")
