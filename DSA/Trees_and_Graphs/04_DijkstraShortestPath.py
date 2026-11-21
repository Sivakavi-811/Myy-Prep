"""
DSA - Trees and Graphs 04: Dijkstra's Shortest Path

Problem:
    Given a weighted directed graph with non-negative edge weights and a
    source vertex, find the shortest distance from the source to every
    vertex, and reconstruct the actual shortest path to a target.

Approach / Intuition:
    Greedy with a min-heap keyed by tentative distance. The vertex popped
    with the smallest distance is final: with non-negative weights, no
    later path can be shorter. Relax its outgoing edges, pushing any
    improved distances. Stale heap entries (distance larger than the best
    already known) are skipped - "lazy deletion" instead of decrease-key.
    Recording each vertex's predecessor lets us rebuild the path.
    (Negative weights break the greedy argument - use Bellman-Ford instead.)

Complexity:
    Time:  O((V + E) log V) with a binary heap
    Space: O(V + E)
"""

import heapq
from typing import Dict, List, Optional, Tuple

Graph = Dict[str, List[Tuple[str, int]]]


def dijkstra(graph: Graph, source: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    dist: Dict[str, float] = {v: float("inf") for v in graph}
    prev: Dict[str, Optional[str]] = {v: None for v in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale entry
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v], prev[v] = nd, u
                heapq.heappush(heap, (nd, v))
    return dist, prev


def path_to(prev: Dict[str, Optional[str]], target: str) -> List[str]:
    path: List[str] = []
    node: Optional[str] = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return path[::-1]


if __name__ == "__main__":
    g: Graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [("E", 3)],
        "E": [],
        "F": [("A", 1)],  # unreachable from A
    }
    dist, prev = dijkstra(g, "A")
    assert dist == {"A": 0, "B": 3, "C": 1, "D": 4, "E": 7, "F": float("inf")}
    assert path_to(prev, "E") == ["A", "C", "B", "D", "E"]
    assert path_to(prev, "A") == ["A"]
    print("All test cases passed!")
