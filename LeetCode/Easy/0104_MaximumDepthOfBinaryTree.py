"""
LeetCode 104. Maximum Depth of Binary Tree (Easy)
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem:
    Given the root of a binary tree, return its maximum depth: the number of
    nodes along the longest path from the root down to a leaf.

Approach / Intuition:
    Recursive DFS: an empty tree has depth 0; otherwise the depth is
    1 + max(depth of left subtree, depth of right subtree).
    An iterative BFS version is also shown - count the levels while
    processing the tree one level at a time.

Complexity:
    Time:  O(n) - every node visited once
    Space: O(h) for DFS (h = tree height), O(w) for BFS (w = max level width)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth, queue = 0, deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


def build(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from LeetCode-style level-order list."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue, i = deque([root]), 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root


if __name__ == "__main__":
    s = Solution()
    for fn in (s.maxDepth, s.maxDepthBFS):
        assert fn(build([3, 9, 20, None, None, 15, 7])) == 3
        assert fn(build([1, None, 2])) == 2
        assert fn(build([])) == 0
    print("All test cases passed!")
