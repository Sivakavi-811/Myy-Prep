"""
DSA - LinkedList 04: Merge Sort on a Linked List

Problem:
    Sort a singly linked list in ascending order in O(n log n) time.

Approach / Intuition:
    Merge sort suits linked lists: splitting needs no random access and
    merging relinks nodes without extra arrays.
      1. Split: find the middle with slow/fast pointers and cut the list.
         Starting fast one step ahead makes slow stop at the end of the
         left half, so a 2-node list splits into 1 + 1.
      2. Recursively sort both halves.
      3. Merge the two sorted halves with a dummy head.

Complexity:
    Time:  O(n log n) - log n levels, O(n) merging per level
    Space: O(log n)   - recursion stack (no auxiliary arrays)
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, next: "Optional[Node]" = None):
        self.val = val
        self.next = next


def merge(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    dummy = tail = Node(0)
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    right = slow.next
    slow.next = None
    return merge(merge_sort(head), merge_sort(right))


def build(values: List[int]) -> Optional[Node]:
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head: Optional[Node]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert to_list(merge_sort(build([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(merge_sort(build([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert to_list(merge_sort(build([2, 1]))) == [1, 2]
    assert to_list(merge_sort(build([3, 3, 1, 1]))) == [1, 1, 3, 3]
    assert merge_sort(None) is None
    print("All test cases passed!")
