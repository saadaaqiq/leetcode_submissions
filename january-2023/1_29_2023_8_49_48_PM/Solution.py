# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self, v=""):
        self.v = v
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("-")

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        if "." not in curr.children:
            curr.children["."] = TrieNode(".")

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return "." in curr.children

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)