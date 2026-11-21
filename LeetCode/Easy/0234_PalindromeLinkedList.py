"""
LeetCode 234. Palindrome Linked List (Easy)
https://leetcode.com/problems/palindrome-linked-list/

Problem:
    Given the head of a singly linked list, return True if it reads the
    same forward and backward. Follow-up: O(n) time and O(1) space.

Approach / Intuition:
    1. Find the middle with slow/fast pointers.
    2. Reverse the second half in place.
    3. Compare the first half with the reversed second half node by node.
    4. Reverse the second half back so the caller's list is left unchanged.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = reverse(slow)

        result, a, b = True, head, second
        while b:
            if a.val != b.val:
                result = False
                break
            a, b = a.next, b.next

        reverse(second)  # restore the original list
        return result


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
    lst = build([1, 2, 2, 1])
    assert s.isPalindrome(lst) is True
    assert to_list(lst) == [1, 2, 2, 1]  # unchanged
    assert s.isPalindrome(build([1, 2])) is False
    assert s.isPalindrome(build([1, 2, 3, 2, 1])) is True
    assert s.isPalindrome(build([1])) is True
    print("All test cases passed!")
