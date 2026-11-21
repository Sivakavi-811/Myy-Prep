"""
LeetCode 21. Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

Problem:
    Given the heads of two sorted singly linked lists, splice them together
    into one sorted list and return its head.

Approach / Intuition:
    Use a dummy head node so we never special-case the first insertion.
    Keep a `tail` pointer; repeatedly attach the smaller of the two current
    nodes and advance that list. When one list runs out, attach the rest of
    the other in one step - it is already sorted.

Complexity:
    Time:  O(n + m) - each node is visited once
    Space: O(1)     - nodes are relinked in place, no new nodes besides dummy
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


def build(values: List[int]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build([]), build([]))) == []
    assert to_list(s.mergeTwoLists(build([]), build([0]))) == [0]
    print("All test cases passed!")
