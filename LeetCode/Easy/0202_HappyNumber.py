"""
LeetCode 202. Happy Number (Easy)
https://leetcode.com/problems/happy-number/

Problem:
    Repeatedly replace n with the sum of the squares of its digits. n is
    "happy" if this process reaches 1; otherwise it loops forever in a
    cycle that doesn't include 1. Return True if n is happy.

Approach / Intuition:
    The sequence either reaches 1 or enters a cycle, which makes it a
    cycle-detection problem: run Floyd's tortoise and hare on the sequence.
    If the fast pointer hits 1 we're done; if slow meets fast elsewhere,
    there is a cycle without 1. This needs no visited set.

Complexity:
    Time:  O(log n) - numbers quickly shrink to below 243, then cycle
    Space: O(1)
"""


def next_number(n: int) -> int:
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d * d
    return total


class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, next_number(n)
        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))
        return fast == 1


if __name__ == "__main__":
    s = Solution()
    assert s.isHappy(19) is True   # 1+81=82 -> 68 -> 100 -> 1
    assert s.isHappy(2) is False
    assert s.isHappy(1) is True
    assert s.isHappy(7) is True
    print("All test cases passed!")
