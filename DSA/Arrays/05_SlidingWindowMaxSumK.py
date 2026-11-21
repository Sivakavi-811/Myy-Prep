"""
DSA - Arrays 05: Sliding Window (Maximum Sum of Size-K Subarray)

Problem:
    Given an array and an integer k, find the maximum sum of any contiguous
    subarray of exactly k elements. Follow-up (variable window): find the
    length of the shortest subarray with sum >= target (positive numbers).

Approach / Intuition:
    Fixed window: compute the first window's sum, then slide one step at a
    time - add the entering element, subtract the leaving one. Each step is
    O(1) instead of re-summing k elements.
    Variable window: expand `right`; while the window sum meets the target,
    record its length and shrink from `left`. Works because all values are
    positive, so shrinking always lowers the sum.

Complexity:
    Time:  O(n) for both - every element enters and leaves the window once
    Space: O(1)
"""

from typing import List


def max_sum_k(arr: List[int], k: int) -> int:
    if k <= 0 or k > len(arr):
        raise ValueError("k must be between 1 and len(arr)")
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best


def min_len_subarray_sum(arr: List[int], target: int) -> int:
    left = total = 0
    best = len(arr) + 1
    for right, x in enumerate(arr):
        total += x
        while total >= target:
            best = min(best, right - left + 1)
            total -= arr[left]
            left += 1
    return best if best <= len(arr) else 0


if __name__ == "__main__":
    assert max_sum_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_k([1, 9, -1, -2, 7, 3, -1, 2], 4) == 13
    assert max_sum_k([5], 1) == 5

    assert min_len_subarray_sum([2, 3, 1, 2, 4, 3], 7) == 2
    assert min_len_subarray_sum([1, 4, 4], 4) == 1
    assert min_len_subarray_sum([1, 1, 1], 11) == 0
    print("All test cases passed!")
