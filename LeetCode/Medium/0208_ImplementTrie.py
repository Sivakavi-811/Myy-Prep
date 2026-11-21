"""
LeetCode 208. Implement Trie (Prefix Tree) (Medium)
https://leetcode.com/problems/implement-trie-prefix-tree/

Problem:
    Implement a trie with insert(word), search(word) (exact match) and
    startsWith(prefix).

Approach / Intuition:
    Each node maps a character to a child node and has an `end` flag that
    marks where a complete word finishes. Insert walks or creates the path
    for each character and sets `end` on the last node. search and
    startsWith share the same walk; search additionally needs the `end`
    flag, so "app" isn't reported just because "apple" was inserted.

Complexity:
    Time:  O(L) per operation - L = length of word/prefix
    Space: O(total characters inserted)
"""

from typing import Dict, Optional


class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def _walk(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.startsWith("b") is False
    assert trie.startsWith("") is True
    print("All test cases passed!")
