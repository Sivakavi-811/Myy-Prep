"""
LeetCode 26. Remove Duplicates from Sorted Array (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Problem:
    Given a sorted array, remove duplicates in place so each unique element
    appears once, keeping order. Return k, the number of unique elements;
    the first k slots of nums must hold them.

Approach / Intuition:
    Because the array is sorted, duplicates sit next to each other.
    `write` points to the slot for the next unique value. Scan with `read`;
    whenever nums[read] differs from the last value written, copy it in.

Complexity:
    Time:  O(n) - single pass
    Space: O(1) - in place
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    s = Solution()
    a = [1, 1, 2]
    k = s.removeDuplicates(a)
    assert k == 2 and a[:k] == [1, 2]

    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(a)
    assert k == 5 and a[:k] == [0, 1, 2, 3, 4]

    assert s.removeDuplicates([]) == 0
    print("All test cases passed!")
