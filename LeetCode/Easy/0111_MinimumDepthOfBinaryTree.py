"""
LeetCode 111. Minimum Depth of Binary Tree (Easy)
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Problem:
    Return the minimum depth of a binary tree: the number of nodes on the
    shortest path from the root down to the nearest leaf.

Approach / Intuition:
    BFS level by level and stop at the first leaf found - that leaf is the
    shallowest, so there is no need to explore deeper parts of the tree.
    (A DFS using min(left, right) must be careful: a node with one missing
    child is NOT a leaf, so the missing side can't count as depth 0.)

Complexity:
    Time:  O(n) worst case, often far less (stops at the first leaf)
    Space: O(w) - the widest level held in the queue
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            for child in (node.left, node.right):
                if child:
                    queue.append((child, depth + 1))
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 2
    chain = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    assert s.minDepth(chain) == 5
    assert s.minDepth(None) == 0
    assert s.minDepth(TreeNode(1, TreeNode(2))) == 2
    print("All test cases passed!")
