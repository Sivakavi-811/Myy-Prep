"""
LeetCode 19. Remove Nth Node From End of List (Medium)
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem:
    Given the head of a linked list, remove the n-th node from the end and
    return the head. Do it in one pass.

Approach / Intuition:
    Two pointers with a gap of n. Advance `fast` n steps ahead, then move
    both until `fast` reaches the last node: `slow` is now just before the
    node to delete. Starting both at a dummy node handles removing the head
    (n == length) without a special case.

Complexity:
    Time:  O(L) - one pass over the list
    Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
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
    assert to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(s.removeNthFromEnd(build([1]), 1)) == []
    assert to_list(s.removeNthFromEnd(build([1, 2]), 1)) == [1]
    assert to_list(s.removeNthFromEnd(build([1, 2]), 2)) == [2]
    print("All test cases passed!")
