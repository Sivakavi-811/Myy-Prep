"""
LeetCode 257. Binary Tree Paths (Easy)
https://leetcode.com/problems/binary-tree-paths/

Problem:
    Return all root-to-leaf paths of a binary tree as strings like "1->2->5".

Approach / Intuition:
    DFS carrying the current path as a list of values. At a leaf, join the
    path into a string and record it. Appending before recursing and
    popping after (backtracking) reuses one list instead of copying
    strings at every level.

Complexity:
    Time:  O(n * h) - n nodes, building each path string costs up to O(h)
    Space: O(h) - recursion depth and path (excluding output)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths: List[str] = []
        path: List[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                paths.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return paths


if __name__ == "__main__":
    s = Solution()
    assert s.binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))) == ["1->2->5", "1->3"]
    assert s.binaryTreePaths(TreeNode(1)) == ["1"]
    assert s.binaryTreePaths(None) == []
    print("All test cases passed!")
