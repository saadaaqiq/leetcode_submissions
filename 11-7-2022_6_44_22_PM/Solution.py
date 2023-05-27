# https://leetcode.com/problems/word-search-ii

class TrieNode:
  def __init__(self, c):
    self.c = c
    self.next = {}

class Trie:
  def __init__(self):
    self.root = TrieNode("-")
  
  def addWords(self, w):
    curr = self.root
    for c in w:
      if c not in curr.next:
        curr.next[c] = TrieNode(c)
      curr = curr.next[c]
    if "." not in curr.next:
      curr.next["."] = TrieNode(".")
  
  def isPrefix(self, w):
    curr = self.root
    for c in w:
      if c not in curr.next:
        return False
      curr = curr.next[c]
    return True
  
  def search(self, w):
    curr = self.root
    for c in w:
      if c not in curr.next:
        return False
      curr = curr.next[c]
    return True if "." in curr.next else False
      
class Solution:
  def findWords(self, board, words):
    m, n = len(board), len(board[0])
    trie = Trie()
    for w in words:
      trie.addWords(w)
    vis = set()

    def dfs(i,j, node):
      nonlocal m, n 
      if (i,j) in vis:
        return False
      vis.add((i,j))
      if "." in node.next:
        node.next.pop(".")
      for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
        if 0<=r<m and 0<=c<n:
          if board[r][c] in node.next and dfs(r,c, node.next[board[r][c]]):
            node.next.pop(board[r][c])
      vis.remove((i,j))
      if len(node.next) == 0:
        return True
      return False
    
    root = trie.root
    res = []

    for i in range(m):
      for j in range(n):
        if board[i][j] in root.next:
          dfs(i,j,root.next[board[i][j]])
    
    for w in words:
      if not trie.search(w):
        res.append(w)

    return res











