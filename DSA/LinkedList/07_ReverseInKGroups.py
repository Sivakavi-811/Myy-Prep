"""
DSA - LinkedList 07: Reverse Nodes in k-Groups

Problem:
    Reverse a linked list k nodes at a time. If the number of remaining
    nodes at the end is less than k, leave them as they are.

Approach / Intuition:
    Process the list group by group, keeping `group_prev` - the node just
    before the current group (a dummy at the start).
      1. Check that k nodes remain; if not, stop.
      2. Reverse those k nodes with the usual prev/cur loop, seeding prev
         with the node after the group so the reversed group stays linked
         to the rest of the list.
      3. Reconnect: group_prev.next becomes the new group head, and the old
         group head (now its tail) becomes group_prev for the next round.

Complexity:
    Time:  O(n) - each node is visited about twice
    Space: O(1)
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, next: "Optional[Node]" = None):
        self.val = val
        self.next = next


def reverse_k_group(head: Optional[Node], k: int) -> Optional[Node]:
    dummy = Node(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        group_next = kth.next

        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            cur.next, prev, cur = prev, cur, cur.next

        old_head = group_prev.next
        group_prev.next = kth
        group_prev = old_head


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
    assert to_list(reverse_k_group(build([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(reverse_k_group(build([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(reverse_k_group(build([1, 2, 3, 4, 5, 6]), 3)) == [3, 2, 1, 6, 5, 4]
    assert to_list(reverse_k_group(build([1, 2]), 1)) == [1, 2]
    assert to_list(reverse_k_group(build([1]), 2)) == [1]
    print("All test cases passed!")
