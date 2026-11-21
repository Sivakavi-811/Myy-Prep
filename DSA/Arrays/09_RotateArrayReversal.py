"""
DSA - Arrays 09: Rotate an Array (Reversal Algorithm)

Problem:
    Rotate an array to the right by k steps, in place, with O(1) extra
    space. Example: [1,2,3,4,5,6,7], k = 3 -> [5,6,7,1,2,3,4].

Approach / Intuition:
    Rotating right by k moves the last k elements to the front. Three
    reversals achieve exactly that:
      1. Reverse the whole array    -> [7,6,5,4,3,2,1]
      2. Reverse the first k        -> [5,6,7,4,3,2,1]
      3. Reverse the remaining n-k  -> [5,6,7,1,2,3,4]
    Take k % n first, since rotating by n is a no-op. Left rotation by k
    equals right rotation by n - k.

Complexity:
    Time:  O(n) - each element moved twice
    Space: O(1)
"""

from typing import List


def reverse(arr: List[int], i: int, j: int) -> None:
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def rotate_right(arr: List[int], k: int) -> None:
    n = len(arr)
    if n == 0:
        return
    k %= n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)


def rotate_left(arr: List[int], k: int) -> None:
    if arr:
        rotate_right(arr, len(arr) - k % len(arr))


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate_right(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]

    a = [-1, -100, 3, 99]
    rotate_right(a, 2)
    assert a == [3, 99, -1, -100]

    a = [1, 2, 3]
    rotate_right(a, 10)  # 10 % 3 = 1
    assert a == [3, 1, 2]

    a = [1, 2, 3, 4, 5]
    rotate_left(a, 2)
    assert a == [3, 4, 5, 1, 2]

    a = []
    rotate_right(a, 4)
    assert a == []
    print("All test cases passed!")
