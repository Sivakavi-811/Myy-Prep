"""
LeetCode 4. Median of Two Sorted Arrays (Hard)
https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem:
    Given two sorted arrays of sizes m and n, return the median of the
    combined data in O(log(m + n)) time.

Approach / Intuition:
    Binary search for a partition. Cut A at i and B at j so the left side
    holds half of all elements: i + j = (m + n + 1) // 2. The partition is
    correct when every left element <= every right element, i.e.
        A[i-1] <= B[j]  and  B[j-1] <= A[i]
    If A[i-1] > B[j], i is too far right; otherwise too far left.
    Searching over the shorter array keeps j in range and gives
    O(log(min(m, n))). The median then comes from the border elements.

Complexity:
    Time:  O(log(min(m, n)))
    Space: O(1)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        inf = float("inf")
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            a_left = A[i - 1] if i > 0 else -inf
            a_right = A[i] if i < m else inf
            b_left = B[j - 1] if j > 0 else -inf
            b_right = B[j] if j < n else inf
            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1
        raise ValueError("input arrays are not sorted")


if __name__ == "__main__":
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert s.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8]) == 4.5
    print("All test cases passed!")
