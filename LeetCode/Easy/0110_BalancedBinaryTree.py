"""
LeetCode 110. Balanced Binary Tree (Easy)
https://leetcode.com/problems/balanced-binary-tree/

Problem:
    Determine whether a binary tree is height-balanced: for every node, the
    heights of its left and right subtrees differ by at most 1.

Approach / Intuition:
    Calling a separate height() at every node costs O(n^2). Instead compute
    heights bottom-up in one DFS and use -1 as a sentinel meaning
    "unbalanced somewhere below". Once a subtree reports -1, propagate it
    straight up without further work.

Complexity:
    Time:  O(n) - each node visited once
    Space: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = height(node.left)
            if left < 0:
                return -1
            right = height(node.right)
            if right < 0 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) >= 0


if __name__ == "__main__":
    s = Solution()
    balanced = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.isBalanced(balanced) is True
    skewed = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    assert s.isBalanced(skewed) is False
    assert s.isBalanced(None) is True
    assert s.isBalanced(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))) is False
    print("All test cases passed!")
