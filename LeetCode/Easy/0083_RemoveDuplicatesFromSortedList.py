"""
LeetCode 83. Remove Duplicates from Sorted List (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Problem:
    Given the head of a sorted linked list, delete duplicates so each value
    appears only once. Return the sorted list.

Approach / Intuition:
    Duplicates are adjacent in a sorted list. Walk with `cur`; while the
    next node has the same value, bypass it. Only advance `cur` once its
    next value differs, so runs of 3+ equal values are fully removed.

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


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
    assert to_list(s.deleteDuplicates(build([1, 1, 2]))) == [1, 2]
    assert to_list(s.deleteDuplicates(build([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert to_list(s.deleteDuplicates(build([1, 1, 1]))) == [1]
    assert s.deleteDuplicates(None) is None
    print("All test cases passed!")
