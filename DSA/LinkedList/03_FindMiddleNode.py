"""
DSA - LinkedList 03: Find the Middle Node

Problem:
    Given the head of a singly linked list, return its middle node. If
    there are two middle nodes (even length), return the second one.

Approach / Intuition:
    Slow and fast pointers: `slow` moves one step, `fast` moves two. When
    `fast` reaches the end, `slow` has covered half the distance and is at
    the middle - one pass, without first counting the length.

Complexity:
    Time:  O(n) - fast traverses the list once
    Space: O(1)
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, next: "Optional[Node]" = None):
        self.val = val
        self.next = next


def middle_node(head: Optional[Node]) -> Optional[Node]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def build(values: List[int]) -> Optional[Node]:
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


if __name__ == "__main__":
    assert middle_node(build([1, 2, 3, 4, 5])).val == 3
    assert middle_node(build([1, 2, 3, 4, 5, 6])).val == 4
    assert middle_node(build([1])).val == 1
    assert middle_node(None) is None
    print("All test cases passed!")
