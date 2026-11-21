"""
DSA - Arrays 03: Sort an Array of 0s, 1s and 2s (Dutch National Flag)

Problem:
    Given an array containing only 0s, 1s and 2s, sort it in place in a single
    pass without using a library sort or counting.

Approach / Intuition (Dijkstra's three-pointer partition):
    Maintain three regions:
        [0 .. low-1]   -> all 0s
        [low .. mid-1] -> all 1s
        [mid .. high]  -> unprocessed
        [high+1 .. n-1]-> all 2s
    Look at arr[mid]:
        0 -> swap with arr[low], advance low and mid
        1 -> already in place, advance mid
        2 -> swap with arr[high], shrink high (do NOT advance mid, because
             the element swapped in from `high` has not been examined yet)
    Stop when mid passes high.

Complexity:
    Time:  O(n)  - each element is examined at most once
    Space: O(1)  - in-place, three pointers
"""

from typing import List


def sort_012(arr: List[int]) -> None:
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


if __name__ == "__main__":
    cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [],
        [2, 2, 1, 1, 0, 0],
        [1, 0, 2, 1, 0, 2, 0, 1],
    ]
    for case in cases:
        expected = sorted(case)
        sort_012(case)
        assert case == expected, (case, expected)
    print("All test cases passed!")
