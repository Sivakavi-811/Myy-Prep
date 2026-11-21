"""
LeetCode 145. Binary Tree Postorder Traversal (Easy)
https://leetcode.com/problems/binary-tree-postorder-traversal/

Problem:
    Return the postorder traversal (left, right, root) of a binary tree.

Approach / Intuition:
    Iterative with one stack and a `last_visited` pointer. Walk down the
    left spine pushing nodes. Peek at the top:
      - If it has a right child we haven't processed yet, go right.
      - Otherwise both subtrees are done: visit it, pop, and remember it as
        last_visited so its parent knows the right side is finished.
    This produces true postorder directly (no reversing trick).

Complexity:
    Time:  O(n)
    Space: O(h) - the stack
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out: List[int] = []
        stack: List[TreeNode] = []
        node, last_visited = root, None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            top = stack[-1]
            if top.right and top.right is not last_visited:
                node = top.right
            else:
                out.append(top.val)
                last_visited = stack.pop()
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [3, 2, 1]
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    assert s.postorderTraversal(root) == [4, 5, 2, 6, 3, 1]
    assert s.postorderTraversal(None) == []
    assert s.postorderTraversal(TreeNode(1)) == [1]
    print("All test cases passed!")
