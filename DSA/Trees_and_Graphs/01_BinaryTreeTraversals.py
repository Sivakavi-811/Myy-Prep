"""
DSA - Trees and Graphs 01: Binary Tree Traversals

Problem:
    Implement the four standard traversals of a binary tree:
    inorder (L, Root, R), preorder (Root, L, R), postorder (L, R, Root)
    and level order (breadth-first, level by level).

Approach / Intuition:
    - The DFS orders differ only in when the root is visited relative to its
      subtrees. Iterative versions use an explicit stack:
        * Inorder: push left spine, pop, visit, then move to right child.
        * Preorder: pop, visit, push right then left (so left is next).
        * Postorder: preorder variant Root, R, L reversed gives L, R, Root.
    - Level order uses a queue and processes one level per outer iteration.

Complexity:
    Time:  O(n) for every traversal - each node handled once
    Space: O(h) for DFS stacks (h = height), O(w) for BFS (w = max width)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]) -> List[int]:
    out, stack, node = [], [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out


def preorder(root: Optional[TreeNode]) -> List[int]:
    out, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out


def postorder(root: Optional[TreeNode]) -> List[int]:
    out, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return out[::-1]


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    levels, queue = [], deque([root] if root else [])
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
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    assert inorder(root) == [4, 2, 5, 1, 3, 6]
    assert preorder(root) == [1, 2, 4, 5, 3, 6]
    assert postorder(root) == [4, 5, 2, 6, 3, 1]
    assert level_order(root) == [[1], [2, 3], [4, 5, 6]]
    for fn in (inorder, preorder, postorder, level_order):
        assert fn(None) == []
    print("All test cases passed!")
