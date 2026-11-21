"""
LeetCode 2. Add Two Numbers (Medium)
https://leetcode.com/problems/add-two-numbers/

Problem:
    Two non-negative integers are stored as linked lists with digits in
    reverse order (ones digit first). Return their sum as a linked list in
    the same format.

Approach / Intuition:
    Reverse order means we can add like on paper, starting from the ones
    place. Walk both lists together, add the digits plus the carry, emit
    total % 10 and carry total // 10. Keep going while either list has
    digits or a carry remains (e.g. 5 + 5 = 10 needs an extra node).

Complexity:
    Time:  O(max(m, n))
    Space: O(max(m, n)) - the result list
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
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
    assert to_list(s.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
    assert to_list(s.addTwoNumbers(build([0]), build([0]))) == [0]
    assert to_list(s.addTwoNumbers(build([9] * 7), build([9] * 4))) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert to_list(s.addTwoNumbers(build([5]), build([5]))) == [0, 1]
    print("All test cases passed!")
