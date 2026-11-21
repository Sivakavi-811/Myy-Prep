"""
DSA - LinkedList 05: Doubly Linked List Implementation

Problem:
    Implement a doubly linked list supporting push/pop at both ends,
    removal of a given node in O(1), and forward/backward traversal.

Approach / Intuition:
    Each node links to both neighbours. Two sentinel nodes (head and tail)
    sit permanently at the ends, so every real node always has a prev and
    a next - insertion and removal never need empty-list or end-of-list
    special cases. This is the structure behind an LRU cache, where O(1)
    removal of an arbitrary node is required.

Complexity:
    Time:  O(1) for push/pop at either end and remove(node); O(n) traversal
    Space: O(n)
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()  # sentinels
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def _insert_after(self, node: Node, val: int) -> Node:
        new = Node(val)
        new.prev, new.next = node, node.next
        node.next.prev = new
        node.next = new
        self.size += 1
        return new

    def push_front(self, val: int) -> Node:
        return self._insert_after(self.head, val)

    def push_back(self, val: int) -> Node:
        return self._insert_after(self.tail.prev, val)

    def remove(self, node: Node) -> int:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.val

    def pop_front(self) -> int:
        if self.size == 0:
            raise IndexError("pop from empty list")
        return self.remove(self.head.next)

    def pop_back(self) -> int:
        if self.size == 0:
            raise IndexError("pop from empty list")
        return self.remove(self.tail.prev)

    def forward(self) -> List[int]:
        out, node = [], self.head.next
        while node is not self.tail:
            out.append(node.val)
            node = node.next
        return out

    def backward(self) -> List[int]:
        out, node = [], self.tail.prev
        while node is not self.head:
            out.append(node.val)
            node = node.prev
        return out


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push_back(2)
    middle = dll.push_back(3)
    dll.push_front(1)
    dll.push_back(4)
    assert dll.forward() == [1, 2, 3, 4]
    assert dll.backward() == [4, 3, 2, 1]

    assert dll.remove(middle) == 3
    assert dll.forward() == [1, 2, 4]
    assert dll.pop_front() == 1
    assert dll.pop_back() == 4
    assert dll.forward() == [2] and dll.size == 1
    dll.pop_back()
    try:
        dll.pop_front()
        raise AssertionError("expected IndexError")
    except IndexError:
        pass
    print("All test cases passed!")
