"""
DSA - Trees and Graphs 05: Topological Sort (Kahn's Algorithm)

Problem:
    Given a directed graph of n tasks and prerequisite edges u -> v
    ("u must come before v"), return a valid ordering of all tasks, or
    report that none exists because the graph has a cycle.

Approach / Intuition:
    Kahn's algorithm (BFS on in-degrees):
      1. Compute each vertex's in-degree (number of prerequisites).
      2. Start a queue with every vertex of in-degree 0 - nothing blocks them.
      3. Pop a vertex, append it to the order, and "remove" its outgoing
         edges by decrementing neighbours' in-degrees; any neighbour that
         drops to 0 becomes available.
      4. If fewer than n vertices were output, the rest are stuck in a cycle.

Complexity:
    Time:  O(V + E)
    Space: O(V + E)
"""

from collections import deque
from typing import List, Optional, Tuple


def topological_sort(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    graph: List[List[int]] = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order: List[int] = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == n else None


def is_valid_order(order: List[int], edges: List[Tuple[int, int]]) -> bool:
    pos = {v: i for i, v in enumerate(order)}
    return all(pos[u] < pos[v] for u, v in edges)


if __name__ == "__main__":
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = topological_sort(6, edges)
    assert order is not None and sorted(order) == list(range(6))
    assert is_valid_order(order, edges)

    assert topological_sort(3, [(0, 1), (1, 2), (2, 0)]) is None  # cycle
    assert topological_sort(3, []) == [0, 1, 2]
    assert topological_sort(2, [(1, 0)]) == [1, 0]
    print("All test cases passed!")
