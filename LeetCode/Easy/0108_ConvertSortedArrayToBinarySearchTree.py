"""
LeetCode 108. Convert Sorted Array to Binary Search Tree (Easy)
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Problem:
    Given a sorted (ascending) integer array, build a height-balanced BST
    from it.

Approach / Intuition:
    Choose the middle element as the root: the elements to its left form
    the left subtree and those to its right form the right subtree, so the
    BST property holds and both sides differ in size by at most one.
    Recurse on index ranges instead of slicing to avoid copying.

Complexity:
    Time:  O(n) - each element becomes one node
    Space: O(log n) - recursion depth of a balanced tree
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            return TreeNode(nums[mid], build(lo, mid - 1), build(mid + 1, hi))

        return build(0, len(nums) - 1)


def inorder(node: Optional[TreeNode]) -> List[int]:
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []


def height(node: Optional[TreeNode]) -> int:
    return 1 + max(height(node.left), height(node.right)) if node else 0


def balanced(node: Optional[TreeNode]) -> bool:
    if node is None:
        return True
    return abs(height(node.left) - height(node.right)) <= 1 and balanced(node.left) and balanced(node.right)


if __name__ == "__main__":
    s = Solution()
    for nums in ([-10, -3, 0, 5, 9], [1, 3], list(range(100)), []):
        root = s.sortedArrayToBST(nums)
        assert inorder(root) == nums
        assert balanced(root)
    print("All test cases passed!")
