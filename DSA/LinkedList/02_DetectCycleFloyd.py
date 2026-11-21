"""
DSA - LinkedList 02: Detect a Cycle (Floyd's Tortoise and Hare)

Problem:
    Given the head of a linked list, determine whether it contains a cycle.
    If it does, return the node where the cycle begins; otherwise None.

Approach / Intuition:
    Move `slow` one step and `fast` two steps at a time. Without a cycle,
    `fast` falls off the end. With a cycle, `fast` gains one node per step
    on `slow` inside the loop, so they must meet.
    Finding the start: let the distance from head to the cycle start be a,
    and from the start to the meeting point be b, with cycle length c.
    Then 2(a + b) = a + b + kc, so a = kc - b. A pointer from the head and a
    pointer from the meeting point, both moving one step, meet exactly at
    the cycle start.

Complexity:
    Time:  O(n) - fast covers at most a couple of laps before meeting
    Space: O(1) - two pointers, no visited set
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[Node] = None


def has_cycle(head: Optional[Node]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def cycle_start(head: Optional[Node]) -> Optional[Node]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            ptr = head
            while ptr is not slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None


def build_with_cycle(values: List[int], pos: int) -> Optional[Node]:
    """Build a list; the tail links back to index `pos` (-1 means no cycle)."""
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    head = build_with_cycle([3, 2, 0, -4], 1)
    assert has_cycle(head) is True
    assert cycle_start(head).val == 2

    head = build_with_cycle([1, 2], 0)
    assert has_cycle(head) is True
    assert cycle_start(head).val == 1

    head = build_with_cycle([1], -1)
    assert has_cycle(head) is False
    assert cycle_start(head) is None

    assert has_cycle(None) is False
    print("All test cases passed!")
