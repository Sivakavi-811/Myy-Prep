"""
DSA - LinkedList 06: LRU Cache (Hash Map + Doubly Linked List)

Problem:
    Design a Least Recently Used cache with a fixed capacity that supports
    get(key) and put(key, value) in O(1). When full, put evicts the least
    recently used key.

Approach / Intuition:
    - A hash map gives O(1) lookup from key to node.
    - A doubly linked list keeps usage order: most recent right after the
      head sentinel, least recent right before the tail sentinel.
    - On every get/put the node is moved to the front (O(1) unlink + link,
      possible only because each node knows its prev).
    - Eviction removes the node before the tail and deletes its map entry,
      which is why the node stores its key too.

Complexity:
    Time:  O(1) for get and put
    Space: O(capacity)
"""

from typing import Dict, Optional


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key, self.val = key, val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: Dict[int, Node] = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _unlink(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _push_front(self, node: Node) -> None:
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self._unlink(node)
        self._push_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._unlink(node)
        else:
            if len(self.map) == self.capacity:
                lru = self.tail.prev
                self._unlink(lru)
                del self.map[lru.key]
            node = Node(key, value)
            self.map[key] = node
        self._push_front(node)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1      # order: 1, 2
    cache.put(3, 3)               # evicts 2
    assert cache.get(2) == -1
    cache.put(4, 4)               # evicts 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)              # update refreshes key 1
    cache.put(3, 3)               # evicts 2, not 1
    assert cache.get(1) == 10 and cache.get(2) == -1
    print("All test cases passed!")
