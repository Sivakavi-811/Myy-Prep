"""
LeetCode 236. Lowest Common Ancestor of a Binary Tree (Medium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Problem:
    Given a binary tree and two nodes p and q in it, return their lowest
    common ancestor: the deepest node that has both p and q as descendants
    (a node counts as a descendant of itself).

Approach / Intuition:
    Recursive search that returns p or q if found in a subtree, else None.
      - If the current node is p or q, return it (it's an ancestor of
        itself, and anything below it can't be a lower LCA).
      - Otherwise search both sides. If both return non-None, p and q are
        on different sides, so this node is the LCA. If only one side is
        non-None, pass that result up.

Complexity:
    Time:  O(n)
    Space: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    n7, n4 = TreeNode(7), TreeNode(4)
    n2 = TreeNode(2, n7, n4)
    n6 = TreeNode(6)
    n5 = TreeNode(5, n6, n2)
    n0, n8 = TreeNode(0), TreeNode(8)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    s = Solution()
    assert s.lowestCommonAncestor(root, n5, n1) is root
    assert s.lowestCommonAncestor(root, n5, n4) is n5   # ancestor of itself
    assert s.lowestCommonAncestor(root, n7, n4) is n2
    assert s.lowestCommonAncestor(root, n6, n4) is n5
    print("All test cases passed!")
