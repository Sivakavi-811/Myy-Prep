"""
DSA - Strings 01: Reverse a String (Two Pointers)

Problem:
    Reverse a string given as a list of characters, in place, using O(1)
    extra memory. Also reverse only the words of a sentence as a follow-up.

Approach / Intuition:
    Place one pointer at each end and swap, moving inward until they meet.
    Each swap fixes two positions, so n/2 swaps are enough.
    Word-order reversal reuses the same helper: reverse the whole sentence,
    then reverse each word back so its letters read forward again.

Complexity:
    Time:  O(n) - every character is swapped at most twice
    Space: O(1) - in-place swaps (the word version works on a char list)
"""

from typing import List


def reverse_range(chars: List[str], i: int, j: int) -> None:
    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1


def reverse_string(chars: List[str]) -> None:
    reverse_range(chars, 0, len(chars) - 1)


def reverse_words(sentence: str) -> str:
    chars = list(" ".join(sentence.split()))
    reverse_range(chars, 0, len(chars) - 1)
    start = 0
    for end in range(len(chars) + 1):
        if end == len(chars) or chars[end] == " ":
            reverse_range(chars, start, end - 1)
            start = end + 1
    return "".join(chars)


if __name__ == "__main__":
    s = list("hello")
    reverse_string(s)
    assert s == list("olleh")

    s = list("Hannah")
    reverse_string(s)
    assert s == list("hannaH")

    empty: List[str] = []
    reverse_string(empty)
    assert empty == []

    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello   world  ") == "world hello"
    print("All test cases passed!")
