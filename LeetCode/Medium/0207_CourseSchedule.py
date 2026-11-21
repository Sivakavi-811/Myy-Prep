"""
LeetCode 207. Course Schedule (Medium)
https://leetcode.com/problems/course-schedule/

Problem:
    There are numCourses courses, and prerequisites[i] = [a, b] means you
    must take b before a. Return True if it's possible to finish them all.

Approach / Intuition:
    All courses can be finished exactly when the prerequisite graph has no
    cycle. Detect cycles with DFS three-colouring:
      0 = unvisited, 1 = on the current DFS path, 2 = fully explored.
    Reaching a node coloured 1 means we found a back edge - a cycle.
    Colour-2 nodes are known safe and are never re-explored.

Complexity:
    Time:  O(V + E)
    Space: O(V + E) - adjacency list, colours and recursion stack
"""

import sys
from typing import List

sys.setrecursionlimit(10_000)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        state = [0] * numCourses

        def has_cycle(u: int) -> bool:
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1 or (state[v] == 0 and has_cycle(v)):
                    return True
            state[u] = 2
            return False

        return not any(state[u] == 0 and has_cycle(u) for u in range(numCourses))


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) is True
    assert s.canFinish(2, [[1, 0], [0, 1]]) is False
    assert s.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) is False
    assert s.canFinish(3, []) is True
    assert s.canFinish(1, [[0, 0]]) is False  # self-loop
    print("All test cases passed!")
