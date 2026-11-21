"""
LeetCode 102. Binary Tree Level Order Traversal (Medium)
https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem:
    Given the root of a binary tree, return its node values level by level,
    left to right, as a list of lists.

Approach / Intuition:
    BFS with a queue. At the start of each round the queue holds exactly
    one level, so record its size and pop that many nodes, collecting their
    values and enqueueing their children for the next round.

Complexity:
    Time:  O(n) - each node enqueued and dequeued once
    Space: O(w) - w = maximum width of the tree (up to n/2)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        levels, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert s.levelOrder(TreeNode(1)) == [[1]]
    assert s.levelOrder(None) == []
    print("All test cases passed!")
