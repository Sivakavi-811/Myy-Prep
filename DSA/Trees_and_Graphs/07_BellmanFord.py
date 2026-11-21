"""
DSA - Trees and Graphs 07: Bellman-Ford Shortest Paths

Problem:
    Find shortest distances from a source in a weighted directed graph that
    may contain NEGATIVE edge weights, and detect negative-weight cycles
    reachable from the source (where shortest paths are undefined).

Approach / Intuition:
    A shortest path without cycles uses at most V - 1 edges. Relaxing every
    edge V - 1 times therefore propagates correct distances along any such
    path, one edge per round. If a V-th round can still improve some
    distance, there must be a reachable negative cycle.
    Early exit: if a whole round makes no change, distances are final.
    (Dijkstra is faster but fails with negative edges, because its greedy
    "popped = final" rule no longer holds.)

Complexity:
    Time:  O(V * E)
    Space: O(V)
"""

from typing import List, Optional, Tuple

Edge = Tuple[int, int, int]  # (u, v, weight)


def bellman_ford(n: int, edges: List[Edge], source: int) -> Optional[List[float]]:
    """Return distances, or None if a negative cycle is reachable."""
    dist = [float("inf")] * n
    dist[source] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist


if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4), (3, 1, 2)]
    assert bellman_ford(4, edges, 0) == [0, 4, 1, 5]

    # negative edge that Dijkstra would mishandle
    assert bellman_ford(3, [(0, 1, 1), (0, 2, 4), (2, 1, -5)], 0) == [0, -1, 4]

    # negative cycle 1 -> 2 -> 1 with total weight -1
    assert bellman_ford(3, [(0, 1, 1), (1, 2, -2), (2, 1, 1)], 0) is None

    # unreachable vertex keeps infinity
    assert bellman_ford(3, [(0, 1, 2)], 0) == [0, 2, float("inf")]
    print("All test cases passed!")
