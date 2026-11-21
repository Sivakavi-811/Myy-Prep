"""
LeetCode 36. Valid Sudoku (Medium)
https://leetcode.com/problems/valid-sudoku/

Problem:
    Determine whether a partially filled 9 x 9 Sudoku board is valid: no
    digit repeats within any row, any column, or any 3 x 3 box. Empty
    cells are '.'. (The board need not be solvable.)

Approach / Intuition:
    One pass over the cells with 27 sets: 9 for rows, 9 for columns,
    9 for boxes. Cell (r, c) belongs to box (r // 3) * 3 + c // 3.
    If a digit is already in its row, column or box set, the board is
    invalid.

Complexity:
    Time:  O(81) = O(1) for a fixed-size board
    Space: O(81) = O(1)
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                b = (r // 3) * 3 + c // 3
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    return False
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)
        return True


if __name__ == "__main__":
    s = Solution()
    valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(valid) is True

    invalid = [row[:] for row in valid]
    invalid[0][0] = "8"  # clashes with the 8 in column 0 and in box 0
    assert s.isValidSudoku(invalid) is False

    box_clash = [["."] * 9 for _ in range(9)]
    box_clash[0][0] = box_clash[1][1] = "4"
    assert s.isValidSudoku(box_clash) is False
    print("All test cases passed!")
