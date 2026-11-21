"""
LeetCode 27. Remove Element (Easy)
https://leetcode.com/problems/remove-element/

Problem:
    Remove every occurrence of `val` from `nums` in place and return k, the
    number of remaining elements. Order of the kept elements may change.

Approach / Intuition:
    Since order doesn't matter, swap unwanted elements with the end of the
    array instead of shifting. `i` scans from the front, `n` is the current
    logical length. When nums[i] == val, overwrite it with the last element
    and shrink n (don't advance i - the moved element still needs checking).
    This does fewer writes than the copy-forward approach when val is rare.

Complexity:
    Time:  O(n) - each step either advances i or shrinks n
    Space: O(1)
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


if __name__ == "__main__":
    s = Solution()
    a = [3, 2, 2, 3]
    k = s.removeElement(a, 3)
    assert k == 2 and sorted(a[:k]) == [2, 2]

    a = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(a, 2)
    assert k == 5 and sorted(a[:k]) == [0, 0, 1, 3, 4]

    assert s.removeElement([], 1) == 0
    assert s.removeElement([1, 1], 1) == 0
    print("All test cases passed!")
