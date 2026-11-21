"""
LeetCode 100. Same Tree (Easy)
https://leetcode.com/problems/same-tree/

Problem:
    Given the roots of two binary trees p and q, return True if they are
    structurally identical and every corresponding node has the same value.

Approach / Intuition:
    Two trees are the same if their roots match and their left subtrees
    are the same and their right subtrees are the same. Base cases: both
    empty -> True; exactly one empty -> False.

Complexity:
    Time:  O(n) - each node pair compared once (stops at first mismatch)
    Space: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()
    assert s.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) is True
    assert s.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))) is False
    assert s.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))) is False
    assert s.isSameTree(None, None) is True
    print("All test cases passed!")
