"""
LeetCode 101. Symmetric Tree (Easy)
https://leetcode.com/problems/symmetric-tree/

Problem:
    Given the root of a binary tree, check whether it is a mirror of itself
    (symmetric around its center).

Approach / Intuition:
    The tree is symmetric if its left and right subtrees mirror each other.
    Two trees a and b are mirrors when a.val == b.val, a.left mirrors
    b.right, and a.right mirrors b.left - compare outer pairs and inner
    pairs together.

Complexity:
    Time:  O(n) - every node visited once
    Space: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None or b is None:
                return a is b
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)

        return root is None or mirror(root.left, root.right)


if __name__ == "__main__":
    s = Solution()
    sym = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert s.isSymmetric(sym) is True
    asym = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert s.isSymmetric(asym) is False
    assert s.isSymmetric(TreeNode(1)) is True
    assert s.isSymmetric(None) is True
    print("All test cases passed!")
