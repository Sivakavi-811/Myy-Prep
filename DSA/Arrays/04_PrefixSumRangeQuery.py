"""
DSA - Arrays 04: Prefix Sum (Range Sum Queries)

Problem:
    Given an array and many queries (l, r), return the sum of
    arr[l..r] (inclusive) for each query efficiently. Follow-up: count the
    subarrays whose sum equals k.

Approach / Intuition:
    Precompute prefix[i] = arr[0] + ... + arr[i-1] (with prefix[0] = 0).
    Then sum(l..r) = prefix[r + 1] - prefix[l], answered in O(1).
    Follow-up: a subarray (j, i] sums to k exactly when
    prefix[i] - prefix[j] == k. While scanning, count how many earlier
    prefix sums equal (current - k) using a hash map.

Complexity:
    Build: O(n) time, O(n) space
    Query: O(1) time
    Subarray-sum-equals-k: O(n) time, O(n) space
"""

from collections import defaultdict
from typing import List


class PrefixSum:
    def __init__(self, arr: List[int]):
        self.prefix = [0]
        for x in arr:
            self.prefix.append(self.prefix[-1] + x)

    def range_sum(self, l: int, r: int) -> int:
        return self.prefix[r + 1] - self.prefix[l]


def count_subarrays_with_sum(arr: List[int], k: int) -> int:
    seen = defaultdict(int)
    seen[0] = 1
    running = count = 0
    for x in arr:
        running += x
        count += seen[running - k]
        seen[running] += 1
    return count


if __name__ == "__main__":
    ps = PrefixSum([-2, 0, 3, -5, 2, -1])
    assert ps.range_sum(0, 2) == 1
    assert ps.range_sum(2, 5) == -1
    assert ps.range_sum(0, 5) == -3
    assert ps.range_sum(3, 3) == -5

    assert count_subarrays_with_sum([1, 1, 1], 2) == 2
    assert count_subarrays_with_sum([1, 2, 3], 3) == 2
    assert count_subarrays_with_sum([1, -1, 0], 0) == 3
    print("All test cases passed!")
