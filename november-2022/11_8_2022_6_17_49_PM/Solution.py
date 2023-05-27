# https://leetcode.com/problems/word-search-ii

class TrieNode:  
  def __init__(self, v):
    self.v = v
    self.next = {}

class Trie:
  def __init__(self):
    self.root = TrieNode("-")
  
  def insert(self, w):
    curr = self.root
    for c in w:
      if c not in curr.next:
        curr.next[c] = TrieNode(c)
      curr = curr.next[c]
    if "." not in curr.next:
      curr.next["."] = TrieNode(".")
  
  def search(self, w):
    curr = self.root
    for c in w:
      if c not in curr.next:
        return False
      curr = curr.next[c]
    return "." in curr.next

class Solution:
  def findWords(self, mat, words):    
    m, n = len(mat), len(mat[0])
    trie = Trie()
    for w in words:
      trie.insert(w)
    vis = set()

    def dfs(i, j, node):
      nonlocal m, n
      if (i,j) in vis:
        return False
      vis.add((i,j))
      if "." in node.next:
        node.next.pop(".")
      for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
        if 0<=r<m and 0<=c<n and mat[r][c] in node.next and dfs(r,c,node.next[mat[r][c]]):
          node.next.pop(mat[r][c])
      vis.remove((i,j))
      if not node.next:
        return True
      return False
    
    for i in range(m):
      for j in range(n):
        if mat[i][j] in trie.root.next:
          if dfs(i, j, trie.root.next[mat[i][j]]):
            trie.root.next.pop(mat[i][j])
    
    res = []

    for w in words:
      if not trie.search(w):
        res.append(w)
    
    return res
















