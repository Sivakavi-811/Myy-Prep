"""
LeetCode 206. Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/

Problem:
    Given the head of a singly linked list, reverse it and return the new
    head.

Approach / Intuition:
    Iterate once, turning each node's next pointer backward. `prev` holds
    the already-reversed prefix; save `cur.next` before overwriting it so
    the rest of the list isn't lost. When `cur` falls off the end, `prev`
    is the new head.

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


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
    assert to_list(s.reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(build([1, 2]))) == [2, 1]
    assert s.reverseList(None) is None
    print("All test cases passed!")
