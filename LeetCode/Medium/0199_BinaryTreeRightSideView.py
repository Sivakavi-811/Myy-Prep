"""
LeetCode 199. Binary Tree Right Side View (Medium)
https://leetcode.com/problems/binary-tree-right-side-view/

Problem:
    Imagine standing on the right side of a binary tree. Return the values
    of the nodes you can see, ordered from top to bottom.

Approach / Intuition:
    The visible node on each level is the rightmost one. DFS visiting the
    right child before the left: the first node reached at each new depth
    is that level's rightmost node, so record it when depth == len(view).

Complexity:
    Time:  O(n)
    Space: O(h) - recursion depth
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view: List[int] = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if depth == len(view):
                view.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return view


if __name__ == "__main__":
    s = Solution()
    assert s.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))) == [1, 3, 4]
    # left subtree deeper: its deepest node is visible
    assert s.rightSideView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))) == [1, 3, 4]
    assert s.rightSideView(TreeNode(1, None, TreeNode(3))) == [1, 3]
    assert s.rightSideView(None) == []
    print("All test cases passed!")
