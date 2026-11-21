"""
LeetCode 200. Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands/

Problem:
    Given an m x n grid of '1' (land) and '0' (water), count the islands.
    An island is a group of land cells connected horizontally or vertically.

Approach / Intuition:
    Scan every cell. When we hit unvisited land, that's a new island:
    increment the count and flood-fill (BFS) all land connected to it,
    marking it as water so it isn't counted again. BFS with an explicit
    queue avoids recursion-depth limits on large grids.

Complexity:
    Time:  O(m * n) - every cell is enqueued at most once
    Space: O(min(m, n)) - BFS frontier (the grid is modified in place)
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                islands += 1
                grid[r][c] = "0"
                queue = deque([(r, c)])
                while queue:
                    x, y = queue.popleft()
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            queue.append((nx, ny))
        return islands


if __name__ == "__main__":
    s = Solution()
    assert s.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]) == 1
    assert s.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3
    assert s.numIslands([["0"]]) == 0
    print("All test cases passed!")
