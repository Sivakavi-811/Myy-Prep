"""
DSA - Trees and Graphs 06: Union-Find (Disjoint Set Union)

Problem:
    Maintain a collection of disjoint sets over n elements supporting
    union(a, b) and find(a) (which set a belongs to). Use it to count
    connected components and detect a cycle in an undirected graph.

Approach / Intuition:
    Each set is a tree; its root is the set's representative.
      - Path compression: during find, point nodes directly at the root
        (here via path halving), flattening the tree for future calls.
      - Union by size: attach the smaller tree under the larger root so
        trees stay shallow.
    Together these give near-constant amortized time per operation.
    Cycle detection: adding edge (u, v) when find(u) == find(v) means u and
    v were already connected - the edge closes a cycle.

Complexity:
    Time:  O(alpha(n)) amortized per operation (inverse Ackermann, <= 4)
    Space: O(n)
"""

from typing import List, Tuple


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def has_cycle(n: int, edges: List[Tuple[int, int]]) -> bool:
    dsu = DSU(n)
    return any(not dsu.union(u, v) for u, v in edges)


if __name__ == "__main__":
    dsu = DSU(6)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    assert dsu.components == 3  # {0,1,2} {3,4} {5}
    assert dsu.find(0) == dsu.find(2)
    assert dsu.find(0) != dsu.find(3)
    assert dsu.union(2, 0) is False  # already connected

    assert has_cycle(3, [(0, 1), (1, 2), (2, 0)]) is True
    assert has_cycle(4, [(0, 1), (1, 2), (2, 3)]) is False
    print("All test cases passed!")
