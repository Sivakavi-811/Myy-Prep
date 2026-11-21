"""
LeetCode 124. Binary Tree Maximum Path Sum (Hard)
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem:
    A path is any sequence of nodes connected by edges, each used at most
    once; it need not pass through the root. Return the maximum sum of any
    non-empty path.

Approach / Intuition:
    For each node compute gain(node): the best sum of a downward path
    starting at that node (it can continue into at most one child).
    Negative child gains are clipped to 0 - better to stop than include.
    The best path that "bends" at this node is
        node.val + gain(left) + gain(right)
    and we update a global maximum with it. The parent only receives
    node.val + max(gain(left), gain(right)), since a path can't fork upward.

Complexity:
    Time:  O(n)
    Space: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    assert s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 42
    assert s.maxPathSum(TreeNode(-3)) == -3
    assert s.maxPathSum(TreeNode(2, TreeNode(-1))) == 2
    print("All test cases passed!")
