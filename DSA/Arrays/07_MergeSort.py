"""
DSA - Arrays 07: Merge Sort (+ Counting Inversions)

Problem:
    Sort an array in O(n log n) with a stable algorithm. Follow-up: count
    inversions - pairs (i, j) with i < j and arr[i] > arr[j] - which measures
    how far the array is from sorted.

Approach / Intuition:
    Divide and conquer: split in half, sort each half recursively, then
    merge the two sorted halves with two pointers. Taking from the left on
    ties (<=) keeps equal elements in order, so the sort is stable.
    Inversions fall out of the merge for free: when an element from the
    right half is placed before the remaining left-half elements, it forms
    an inversion with every one of them (len(left) - i of them).

Complexity:
    Time:  O(n log n) - log n levels, O(n) merge work per level
    Space: O(n)       - temporary arrays during merging
"""

from typing import List, Tuple


def merge_sort_count(arr: List[int]) -> Tuple[List[int], int]:
    if len(arr) <= 1:
        return arr[:], 0
    mid = len(arr) // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])

    merged, i, j, inversions = [], 0, 0, inv_left + inv_right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


def merge_sort(arr: List[int]) -> List[int]:
    return merge_sort_count(arr)[0]


if __name__ == "__main__":
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([]) == []
    assert merge_sort([5, -1, 5, 0]) == [-1, 0, 5, 5]

    assert merge_sort_count([2, 4, 1, 3, 5])[1] == 3   # (2,1) (4,1) (4,3)
    assert merge_sort_count([5, 4, 3, 2, 1])[1] == 10  # fully reversed: n(n-1)/2
    assert merge_sort_count([1, 2, 3])[1] == 0
    print("All test cases passed!")
