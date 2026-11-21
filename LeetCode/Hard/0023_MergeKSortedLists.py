"""
LeetCode 23. Merge k Sorted Lists (Hard)
https://leetcode.com/problems/merge-k-sorted-lists/

Problem:
    Given an array of k sorted linked lists, merge them into one sorted
    linked list and return its head.

Approach / Intuition:
    Keep a min-heap holding the current head of each non-empty list.
    Repeatedly pop the smallest node, append it to the result, and push
    that node's successor. The heap never holds more than k nodes.
    The list index is stored as a tie-breaker so the heap never has to
    compare ListNode objects directly.

Complexity:
    Time:  O(N log k) - N total nodes, each push/pop costs O(log k)
    Space: O(k) - the heap
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = tail = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
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
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    assert to_list(s.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(s.mergeKLists([])) == []
    assert to_list(s.mergeKLists([None])) == []
    assert to_list(s.mergeKLists([build([2]), None, build([-1])])) == [-1, 2]
    print("All test cases passed!")
