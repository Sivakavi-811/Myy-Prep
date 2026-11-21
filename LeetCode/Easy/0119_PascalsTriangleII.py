"""
LeetCode 119. Pascal's Triangle II (Easy)
https://leetcode.com/problems/pascals-triangle-ii/

Problem:
    Return the rowIndex-th (0-indexed) row of Pascal's triangle using only
    O(rowIndex) extra space.

Approach / Intuition:
    Update a single row in place from RIGHT to LEFT:
        row[j] += row[j - 1]
    Going right-to-left means row[j - 1] still holds the previous row's
    value when we read it (left-to-right would use already-updated values).
    Append a 1 at the end for each new row.

Complexity:
    Time:  O(rowIndex^2)
    Space: O(rowIndex)
"""

from math import comb
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            for j in range(len(row) - 1, 0, -1):
                row[j] += row[j - 1]
            row.append(1)
        return row


if __name__ == "__main__":
    s = Solution()
    assert s.getRow(3) == [1, 3, 3, 1]
    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1, 1]
    assert s.getRow(20) == [comb(20, k) for k in range(21)]
    print("All test cases passed!")
