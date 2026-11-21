"""
DSA - Arrays 06: Next Greater Element (Monotonic Stack)

Problem:
    For every element in an array, find the first element to its right that
    is strictly greater; use -1 if none exists. Follow-up: the same for a
    circular array, where the search wraps around to the start.

Approach / Intuition:
    Keep a stack of indices whose next-greater element hasn't been found
    yet. Their values are decreasing from bottom to top (a "monotonic
    stack"). When a new value is bigger than the top, it is the answer for
    that index - pop and record, repeating while it stays bigger.
    Circular version: iterate over 2n positions (i % n) so elements near
    the end can see the elements at the start; only push during the first
    pass.

Complexity:
    Time:  O(n) - every index is pushed and popped at most once
    Space: O(n) - the stack and answer array
"""

from typing import List


def next_greater(arr: List[int]) -> List[int]:
    result = [-1] * len(arr)
    stack: List[int] = []
    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result


def next_greater_circular(arr: List[int]) -> List[int]:
    n = len(arr)
    result = [-1] * n
    stack: List[int] = []
    for i in range(2 * n):
        x = arr[i % n]
        while stack and arr[stack[-1]] < x:
            result[stack.pop()] = x
        if i < n:
            stack.append(i)
    return result


if __name__ == "__main__":
    assert next_greater([4, 5, 2, 25]) == [5, 25, 25, -1]
    assert next_greater([13, 7, 6, 12]) == [-1, 12, 12, -1]
    assert next_greater([1, 1, 1]) == [-1, -1, -1]
    assert next_greater([]) == []

    assert next_greater_circular([1, 2, 1]) == [2, -1, 2]
    assert next_greater_circular([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
    print("All test cases passed!")
