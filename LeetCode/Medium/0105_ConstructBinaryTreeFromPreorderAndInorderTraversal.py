"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem:
    Given the preorder and inorder traversals of a binary tree with unique
    values, reconstruct and return the tree.

Approach / Intuition:
    The next unused preorder value is always the root of the current
    subtree. Its position in the inorder list splits that subtree's range
    into left (before it) and right (after it). Recurse left first, then
    right - matching preorder's order. A value -> inorder-index map makes
    each split O(1) instead of a linear search.

Complexity:
    Time:  O(n)
    Space: O(n) - the index map plus O(h) recursion
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {v: i for i, v in enumerate(inorder)}
        pre = iter(preorder)

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            root = TreeNode(next(pre))
            mid = index[root.val]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)


def level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    out, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.extend((node.left, node.right))
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    s = Solution()
    assert level_order(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
    assert level_order(s.buildTree([-1], [-1])) == [-1]
    assert level_order(s.buildTree([1, 2, 3], [3, 2, 1])) == [1, 2, None, 3]
    print("All test cases passed!")
