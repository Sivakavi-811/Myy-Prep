"""
LeetCode 94. Binary Tree Inorder Traversal (Easy)
https://leetcode.com/problems/binary-tree-inorder-traversal/

Problem:
    Return the inorder traversal (left, root, right) of a binary tree's
    node values.

Approach / Intuition:
    Morris traversal - O(1) extra space, no stack or recursion. For each
    node with a left subtree, find its inorder predecessor (rightmost node
    of the left subtree):
      - If the predecessor's right pointer is empty, thread it back to the
        current node and go left.
      - If it already points to the current node, the left subtree is done:
        remove the thread, visit the node, and go right.
    Every thread is created and removed once, restoring the tree.

Complexity:
    Time:  O(n) - each edge traversed at most a constant number of times
    Space: O(1) - excluding the output
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out: List[int] = []
        cur = root
        while cur:
            if cur.left is None:
                out.append(cur.val)
                cur = cur.right
                continue
            pred = cur.left
            while pred.right and pred.right is not cur:
                pred = pred.right
            if pred.right is None:
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                out.append(cur.val)
                cur = cur.right
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 3, 2]
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    assert s.inorderTraversal(root) == [1, 2, 3, 4, 5, 6, 7]
    assert s.inorderTraversal(root) == [1, 2, 3, 4, 5, 6, 7]  # tree restored
    assert s.inorderTraversal(None) == []
    print("All test cases passed!")
