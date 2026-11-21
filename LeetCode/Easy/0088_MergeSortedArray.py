"""
LeetCode 88. Merge Sorted Array (Easy)
https://leetcode.com/problems/merge-sorted-array/

Problem:
    nums1 has length m + n: its first m elements are sorted and the last n
    are zero placeholders. nums2 holds n sorted elements. Merge nums2 into
    nums1 in place so nums1 ends up sorted.

Approach / Intuition:
    Fill nums1 from the back. Compare the largest unplaced elements of each
    array and write the bigger one at position k (the last free slot).
    Writing from the back never overwrites an unread nums1 element.
    If nums2 still has elements at the end, copy them; leftover nums1
    elements are already in place.

Complexity:
    Time:  O(m + n) - each element placed once
    Space: O(1)     - in place
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 0, 0, 0]
    s.merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]

    a = [1]
    s.merge(a, 1, [], 0)
    assert a == [1]

    a = [0]
    s.merge(a, 0, [1], 1)
    assert a == [1]

    a = [4, 5, 6, 0, 0, 0]
    s.merge(a, 3, [1, 2, 3], 3)
    assert a == [1, 2, 3, 4, 5, 6]
    print("All test cases passed!")
