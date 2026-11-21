"""
LeetCode 112. Path Sum (Easy)
https://leetcode.com/problems/path-sum/

Problem:
    Given a binary tree and an integer targetSum, return True if some
    root-to-leaf path has node values adding up to targetSum.

Approach / Intuition:
    Subtract each node's value from the remaining target as we go down.
    At a leaf, the path works exactly when the remainder equals the leaf's
    value. The check must happen only at leaves - a path that stops at an
    internal node doesn't count.

Complexity:
    Time:  O(n) - each node visited at most once
    Space: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5,
                    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert s.hasPathSum(root, 22) is True
    assert s.hasPathSum(root, 26) is True
    assert s.hasPathSum(root, 9) is False  # 5 -> 4 stops at internal node
    assert s.hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5) is False
    assert s.hasPathSum(None, 0) is False
    print("All test cases passed!")
