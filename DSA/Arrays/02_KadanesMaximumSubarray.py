"""
DSA - Arrays 02: Maximum Subarray Sum (Kadane's Algorithm)

Problem:
    Given an integer array (which may contain negatives), find the contiguous
    non-empty subarray with the largest sum and return that sum. Also return
    the subarray's start and end indices.

Approach / Intuition:
    At each index i, the best subarray ending at i either:
      - extends the best subarray ending at i-1, or
      - starts fresh at i (when the running sum so far is negative and would
        only drag the total down).
    So: current = max(nums[i], current + nums[i]), and track the global best.
    Initialising with nums[0] (not 0) correctly handles all-negative arrays.

Complexity:
    Time:  O(n)  - single pass
    Space: O(1)  - a few variables
"""

from typing import List, Tuple


def max_subarray(nums: List[int]) -> Tuple[int, int, int]:
    """Return (max_sum, start_index, end_index)."""
    if not nums:
        raise ValueError("Array must be non-empty")

    best = current = nums[0]
    best_start = best_end = start = 0

    for i in range(1, len(nums)):
        if current < 0:
            current = nums[i]
            start = i
        else:
            current += nums[i]

        if current > best:
            best = current
            best_start, best_end = start, i

    return best, best_start, best_end


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == (6, 3, 6)  # [4,-1,2,1]
    assert max_subarray([1]) == (1, 0, 0)
    assert max_subarray([5, 4, -1, 7, 8]) == (23, 0, 4)
    assert max_subarray([-3, -1, -2]) == (-1, 1, 1)  # all negative
    print("All test cases passed!")
