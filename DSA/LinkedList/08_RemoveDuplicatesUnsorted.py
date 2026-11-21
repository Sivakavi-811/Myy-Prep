"""
DSA - LinkedList 08: Remove Duplicates from an Unsorted Linked List

Problem:
    Remove duplicate values from an unsorted singly linked list, keeping
    the first occurrence of each value. Follow-up: do it without extra
    memory.

Approach / Intuition:
    1. Hash set (O(n) time): walk the list remembering seen values; when
       the next node's value was already seen, unlink it.
    2. No extra memory (O(n^2) time): for each node, use a "runner"
       pointer to scan and unlink later nodes with the same value.
    Both keep the first occurrence because removal only ever happens to
    nodes *after* the one that introduced the value.

Complexity:
    Hash set:  O(n) time, O(n) space
    Runner:    O(n^2) time, O(1) space
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, next: "Optional[Node]" = None):
        self.val = val
        self.next = next


def remove_dups_hash(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None
    seen = {head.val}
    cur = head
    while cur.next:
        if cur.next.val in seen:
            cur.next = cur.next.next
        else:
            seen.add(cur.next.val)
            cur = cur.next
    return head


def remove_dups_runner(head: Optional[Node]) -> Optional[Node]:
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.val == cur.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head


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
    for fn in (remove_dups_hash, remove_dups_runner):
        assert to_list(fn(build([5, 2, 2, 4, 5, 1]))) == [5, 2, 4, 1]
        assert to_list(fn(build([1, 1, 1]))) == [1]
        assert to_list(fn(build([3, 1, 2]))) == [3, 1, 2]
        assert fn(None) is None
    print("All test cases passed!")
