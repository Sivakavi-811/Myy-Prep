"""
LeetCode 203. Remove Linked List Elements (Easy)
https://leetcode.com/problems/remove-linked-list-elements/

Problem:
    Remove every node whose value equals `val` from a linked list and
    return the new head.

Approach / Intuition:
    A dummy node before the head means removing the head (even several
    heads in a row) is no different from removing any other node. Walk
    with `cur`: if cur.next matches, unlink it (don't advance - the new
    cur.next may also match); otherwise advance.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0, head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


def build(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.removeElements(build([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert to_list(s.removeElements(build([]), 1)) == []
    assert to_list(s.removeElements(build([7, 7, 7, 7]), 7)) == []
    assert to_list(s.removeElements(build([1, 7, 7, 2]), 7)) == [1, 2]
    print("All test cases passed!")
