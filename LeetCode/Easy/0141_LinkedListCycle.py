"""
LeetCode 141. Linked List Cycle (Easy)
https://leetcode.com/problems/linked-list-cycle/

Problem:
    Given the head of a linked list, return True if the list has a cycle
    (some node can be reached again by following next pointers).

Approach / Intuition:
    Floyd's tortoise and hare: slow moves 1 step, fast moves 2. Without a
    cycle, fast reaches the end. With one, fast laps slow inside the loop
    and they meet, because the gap closes by exactly one node per step.

Complexity:
    Time:  O(n)
    Space: O(1) - no visited set needed
"""

from typing import List, Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def build(values: List[int], pos: int) -> Optional[ListNode]:
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    s = Solution()
    assert s.hasCycle(build([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(build([1, 2], 0)) is True
    assert s.hasCycle(build([1], -1)) is False
    assert s.hasCycle(build([1, 2, 3], -1)) is False
    assert s.hasCycle(None) is False
    print("All test cases passed!")
