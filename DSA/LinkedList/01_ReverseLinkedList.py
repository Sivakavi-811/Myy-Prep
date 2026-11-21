"""
DSA - LinkedList 01: Reverse a Singly Linked List

Problem:
    Given the head of a singly linked list, reverse the list and return the
    new head.

Approach / Intuition:
    Walk the list once, flipping each `next` pointer to point backward.
    Three pointers are enough: `prev` (already-reversed part), `cur` (node
    being flipped) and `nxt` (saved so we don't lose the rest of the list).
    The recursive version reverses the tail first, then hooks the current
    node onto the end of it.

Complexity:
    Time:  O(n) - every node is visited once
    Space: O(1) iterative, O(n) recursive (call stack)
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, next: "Optional[Node]" = None):
        self.val = val
        self.next = next


def reverse_iterative(head: Optional[Node]) -> Optional[Node]:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev


def reverse_recursive(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


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
    for fn in (reverse_iterative, reverse_recursive):
        assert to_list(fn(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
        assert to_list(fn(build([1, 2]))) == [2, 1]
        assert to_list(fn(build([7]))) == [7]
        assert fn(None) is None
    print("All test cases passed!")
