"""
LeetCode 98. Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

Problem:
    Determine whether a binary tree is a valid BST: every node's left
    subtree holds only smaller keys, its right subtree only larger keys,
    and both subtrees are BSTs themselves.

Approach / Intuition:
    Checking only a node against its direct children is not enough - a
    deep node must respect every ancestor. Pass down an open interval
    (low, high) of allowed values: going left tightens `high` to the parent's
    value, going right tightens `low`. Any node outside its interval fails.

Complexity:
    Time:  O(n) - each node checked once
    Space: O(h) - recursion depth, h = tree height
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    s = Solution()
    assert s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))) is True
    # 5 -> right child 4 < 5: invalid
    assert s.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) is False
    # 3 sits in 5's right subtree but is < 5: invalid (deep-ancestor case)
    assert s.isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))) is False
    assert s.isValidBST(TreeNode(1, TreeNode(1))) is False  # duplicates not allowed
    assert s.isValidBST(None) is True
    print("All test cases passed!")
