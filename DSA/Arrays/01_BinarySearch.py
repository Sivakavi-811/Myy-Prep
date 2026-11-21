"""
DSA - Arrays 01: Binary Search

Problem:
    Given a sorted (ascending) array of distinct integers and a target, return
    the index of the target, or -1 if it is not present.

Approach / Intuition:
    Because the array is sorted, comparing the target with the middle element
    tells us which half can be discarded. Repeat on the remaining half until
    the search range is empty.
      - Use the inclusive range [lo, hi] and loop while lo <= hi.
      - mid = lo + (hi - lo) // 2 avoids overflow in fixed-width languages
        (a good habit even though Python ints don't overflow).
    Both iterative and recursive versions are shown; the iterative one is
    preferred because it uses O(1) space.

Complexity:
    Time:  O(log n) - the search space halves every step
    Space: O(1) iterative, O(log n) recursive (call stack)
"""

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(arr: List[int], target: int, lo: int = 0, hi: int = None) -> int:
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    return binary_search_recursive(arr, target, lo, mid - 1)


if __name__ == "__main__":
    data = [-1, 0, 3, 5, 9, 12]
    for fn in (binary_search, binary_search_recursive):
        assert fn(data, 9) == 4
        assert fn(data, 2) == -1
        assert fn(data, -1) == 0
        assert fn(data, 12) == 5
        assert fn([], 1) == -1
        assert fn([7], 7) == 0
    print("All test cases passed!")
