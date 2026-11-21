"""
LeetCode 230. Kth Smallest Element in a BST (Medium)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem:
    Given the root of a BST and an integer k, return the k-th smallest
    value (1-indexed).

Approach / Intuition:
    An inorder traversal of a BST visits values in ascending order. Run an
    iterative inorder walk and stop as soon as the k-th node is popped -
    no need to traverse the rest of the tree.

Complexity:
    Time:  O(h + k) - descend to the minimum, then k steps
    Space: O(h) - the stack
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack: List[TreeNode] = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert s.kthSmallest(root, 1) == 1
    assert s.kthSmallest(root, 3) == 3
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert [s.kthSmallest(root, k) for k in range(1, 7)] == [1, 2, 3, 4, 5, 6]
    print("All test cases passed!")
