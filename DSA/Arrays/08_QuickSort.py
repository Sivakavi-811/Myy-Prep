"""
DSA - Arrays 08: Quick Sort (+ Quickselect)

Problem:
    Sort an array in place in O(n log n) expected time. Follow-up: find the
    k-th smallest element in O(n) expected time without fully sorting.

Approach / Intuition:
    Pick a pivot and partition (Lomuto scheme): move everything smaller
    than the pivot to the left, then put the pivot right after them - it is
    now in its final sorted position. Recurse on both sides.
    A random pivot makes the O(n^2) worst case (e.g. already-sorted input
    with a fixed pivot) vanishingly unlikely.
    Quickselect partitions the same way but recurses into only the side
    that contains index k.

Complexity:
    Quick sort:  O(n log n) expected, O(n^2) worst; O(log n) stack expected
    Quickselect: O(n) expected, O(n^2) worst; O(1) extra (iterative)
"""

import random
from typing import List


def partition(arr: List[int], lo: int, hi: int) -> int:
    p = random.randint(lo, hi)
    arr[p], arr[hi] = arr[hi], arr[p]
    pivot, store = arr[hi], lo
    for i in range(lo, hi):
        if arr[i] < pivot:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1
    arr[store], arr[hi] = arr[hi], arr[store]
    return store


def quick_sort(arr: List[int], lo: int = 0, hi: int = None) -> None:
    if hi is None:
        hi = len(arr) - 1
    while lo < hi:
        p = partition(arr, lo, hi)
        # recurse into the smaller side, loop on the larger: O(log n) stack
        if p - lo < hi - p:
            quick_sort(arr, lo, p - 1)
            lo = p + 1
        else:
            quick_sort(arr, p + 1, hi)
            hi = p - 1


def quickselect(arr: List[int], k: int) -> int:
    """Return the k-th smallest (0-indexed) element. Reorders arr."""
    lo, hi = 0, len(arr) - 1
    while True:
        p = partition(arr, lo, hi)
        if p == k:
            return arr[p]
        if p < k:
            lo = p + 1
        else:
            hi = p - 1


if __name__ == "__main__":
    random.seed(7)
    for data in ([10, 7, 8, 9, 1, 5], [], [1], [3, 3, 3], list(range(500, 0, -1))):
        expected = sorted(data)
        quick_sort(data)
        assert data == expected

    nums = [7, 10, 4, 3, 20, 15]
    assert quickselect(nums[:], 2) == 7
    assert quickselect(nums[:], 0) == 3
    assert quickselect(nums[:], 5) == 20
    print("All test cases passed!")
