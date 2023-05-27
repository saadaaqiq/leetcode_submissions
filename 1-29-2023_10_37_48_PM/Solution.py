# https://leetcode.com/problems/design-add-and-search-words-data-structure

class TrieNode:
    def __init__(self, v=""):
        self.v = v
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode("-")

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.children["_"] = TrieNode("_")

    def search(self, word: str) -> bool:
        stack = [(0, self.root)]
        while stack:
            i, curr = stack.pop()
            if i == len(word):
                if "_" in curr.children:
                    return True
                else:
                    continue
            if word[i] == ".":
                for k in curr.children:
                    if k != "_":
                        stack.append((i+1, curr.children[k]))
            else:
                if word[i] in curr.children:
                    stack.append((i+1, curr.children[word[i]]))
        return False

            

    







