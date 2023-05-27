# https://leetcode.com/problems/design-add-and-search-words-data-structure

class TrieNode:
    def __init__(self):
        self.eow = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:

        def sub_search(w, cur):
            if not w:
                return cur.eow
            if w[0] in cur.children:
                return sub_search(w[1:], cur.children[w[0]])
            elif w[0] == ".":
                for x in cur.children:
                    if sub_search(w[1:], cur.children[x]):
                        return True
                return False
            else:
                return False
            
        return sub_search(word, self.root)




                

