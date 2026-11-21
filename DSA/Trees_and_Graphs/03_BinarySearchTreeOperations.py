"""
DSA - Trees and Graphs 03: Binary Search Tree (Insert, Search, Delete)

Problem:
    Implement a binary search tree supporting insert, search and delete,
    keeping the BST property (left < node < right) after every operation.

Approach / Intuition:
    - Search/Insert: compare with the current node and go left or right;
      insert attaches a new leaf where the search falls off the tree.
    - Delete has three cases:
        1. Leaf: just remove it.
        2. One child: replace the node with that child.
        3. Two children: copy in the inorder successor (smallest value in
           the right subtree), then delete that successor from the right
           subtree - it has at most one child, so it falls into case 1/2.

Complexity:
    Time:  O(h) per operation - O(log n) balanced, O(n) worst case (skewed)
    Space: O(h) - recursion depth
"""

from typing import List, Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def insert(root: Optional[Node], key: int) -> Node:
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root  # duplicates are ignored


def search(root: Optional[Node], key: int) -> bool:
    while root:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False


def delete(root: Optional[Node], key: int) -> Optional[Node]:
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        succ = root.right
        while succ.left:
            succ = succ.left
        root.key = succ.key
        root.right = delete(root.right, succ.key)
    return root


def inorder(root: Optional[Node]) -> List[int]:
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []


if __name__ == "__main__":
    root = None
    for k in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, k)
    assert inorder(root) == [20, 30, 40, 50, 60, 70, 80]
    assert search(root, 60) and not search(root, 65)

    root = delete(root, 20)   # leaf
    assert inorder(root) == [30, 40, 50, 60, 70, 80]
    root = delete(root, 30)   # one child
    assert inorder(root) == [40, 50, 60, 70, 80]
    root = delete(root, 50)   # two children (root)
    assert inorder(root) == [40, 60, 70, 80]
    assert root.key == 60
    root = delete(root, 999)  # missing key: no change
    assert inorder(root) == [40, 60, 70, 80]
    print("All test cases passed!")
