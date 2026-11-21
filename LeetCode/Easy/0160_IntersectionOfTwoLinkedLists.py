"""
LeetCode 160. Intersection of Two Linked Lists (Easy)
https://leetcode.com/problems/intersection-of-two-linked-lists/

Problem:
    Given the heads of two singly linked lists, return the node where they
    intersect (the first shared node by identity), or None.

Approach / Intuition:
    Two pointers that switch lists. Pointer a walks A then B; pointer b
    walks B then A. Both travel lenA + lenB nodes in total, so they line up
    at the same distance from the end: they meet at the intersection, or
    both reach None together if the lists never meet. No length counting
    is needed.

Complexity:
    Time:  O(m + n)
    Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, x: int, next: "Optional[ListNode]" = None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


if __name__ == "__main__":
    s = Solution()
    shared = ListNode(8, ListNode(4, ListNode(5)))
    A = ListNode(4, ListNode(1, shared))
    B = ListNode(5, ListNode(6, ListNode(1, shared)))
    assert s.getIntersectionNode(A, B) is shared

    assert s.getIntersectionNode(ListNode(2, ListNode(6, ListNode(4))), ListNode(1, ListNode(5))) is None

    same = ListNode(1)
    assert s.getIntersectionNode(same, same) is same
    print("All test cases passed!")
