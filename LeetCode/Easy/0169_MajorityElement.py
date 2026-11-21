"""
LeetCode 169. Majority Element (Easy)
https://leetcode.com/problems/majority-element/

Problem:
    Given an array of size n, return the element that appears more than
    n / 2 times. The majority element is guaranteed to exist.

Approach / Intuition:
    Boyer-Moore Voting. Keep a `candidate` and a `count`. Matching elements
    vote +1, others vote -1; when the count hits 0, pick the current element
    as the new candidate. Every non-majority vote can cancel at most one
    majority vote, and the majority has more than half the votes, so it
    survives as the final candidate.

Complexity:
    Time:  O(n) - one pass
    Space: O(1) - two variables
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([7]) == 7
    print("All test cases passed!")
