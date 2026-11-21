"""
DSA - Trees and Graphs 02: Graph BFS and DFS

Problem:
    Given an undirected graph as an adjacency list, implement breadth-first
    and depth-first traversal from a start vertex, plus shortest path
    (fewest edges) between two vertices using BFS.

Approach / Intuition:
    - BFS explores the graph in rings of increasing distance using a queue.
      Because the first time BFS reaches a vertex is via the fewest edges,
      recording each vertex's parent lets us rebuild the shortest path.
    - DFS goes as deep as possible before backtracking (recursion here).
    - Mark vertices visited when they are *enqueued*/entered so nothing is
      processed twice, even in graphs with cycles.

Complexity:
    Time:  O(V + E) - each vertex and edge is examined once
    Space: O(V)     - visited set, queue/recursion stack, parent map
"""

from collections import deque
from typing import Dict, List, Optional

Graph = Dict[int, List[int]]


def bfs(graph: Graph, start: int) -> List[int]:
    order, visited, queue = [], {start}, deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order


def dfs(graph: Graph, start: int) -> List[int]:
    order, visited = [], set()

    def visit(v: int) -> None:
        visited.add(v)
        order.append(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                visit(nb)

    visit(start)
    return order


def shortest_path(graph: Graph, src: int, dst: int) -> Optional[List[int]]:
    parent = {src: None}
    queue = deque([src])
    while queue:
        v = queue.popleft()
        if v == dst:
            path = []
            while v is not None:
                path.append(v)
                v = parent[v]
            return path[::-1]
        for nb in graph.get(v, []):
            if nb not in parent:
                parent[nb] = v
                queue.append(nb)
    return None


if __name__ == "__main__":
    # 0 - 1 - 3
    # |   |
    # 2 - 4    5 (isolated)
    g: Graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1], 4: [1, 2], 5: []}
    assert bfs(g, 0) == [0, 1, 2, 3, 4]
    assert dfs(g, 0) == [0, 1, 3, 4, 2]
    assert shortest_path(g, 0, 3) == [0, 1, 3]
    assert shortest_path(g, 2, 3) in ([2, 0, 1, 3], [2, 4, 1, 3])
    assert shortest_path(g, 0, 5) is None
    assert shortest_path(g, 4, 4) == [4]
    print("All test cases passed!")
