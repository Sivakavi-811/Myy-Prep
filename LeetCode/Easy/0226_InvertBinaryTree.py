"""
LeetCode 226. Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

Problem:
    Given the root of a binary tree, invert it (mirror it left-to-right)
    and return its root.

Approach / Intuition:
    Mirroring a tree = swap the children of every node. Do it recursively:
    invert both subtrees, then swap them. Order doesn't matter as long as
    every node gets its children swapped exactly once.

Complexity:
    Time:  O(n) - each node visited once
    Space: O(h) - recursion stack, h = tree height
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def build(values: List[Optional[int]]) -> Optional[TreeNode]:
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


def level_order(root: Optional[TreeNode]) -> List[int]:
    out, queue = [], deque([root] if root else [])
    while queue:
        node = queue.popleft()
        out.append(node.val)
        queue.extend(c for c in (node.left, node.right) if c)
    return out


if __name__ == "__main__":
    s = Solution()
    assert level_order(s.invertTree(build([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert level_order(s.invertTree(build([2, 1, 3]))) == [2, 3, 1]
    assert s.invertTree(None) is None
    print("All test cases passed!")
