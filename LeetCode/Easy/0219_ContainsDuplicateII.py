"""
LeetCode 219. Contains Duplicate II (Easy)
https://leetcode.com/problems/contains-duplicate-ii/

Problem:
    Return True if there are two distinct indices i and j with
    nums[i] == nums[j] and |i - j| <= k.

Approach / Intuition:
    Sliding window of the last k elements kept in a set. For each element,
    if it's already in the window, a close-enough duplicate exists.
    Otherwise add it and evict the element that just fell out of range
    (index i - k), keeping the set at most k elements.

Complexity:
    Time:  O(n)
    Space: O(min(n, k))
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, x in enumerate(nums):
            if x in window:
                return True
            window.add(x)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert s.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert s.containsNearbyDuplicate([1, 1], 0) is False
    print("All test cases passed!")
