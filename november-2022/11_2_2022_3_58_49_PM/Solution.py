# https://leetcode.com/problems/alien-dictionary

class Solution:
  def alienOrder(self, words: List[str]) -> str:
    m = len(words)
    adj = {words[i][j]: set() for i in range(m) for j in range(len(words[i]))}
    for i in range(m-1):
      j = 0 
      lc, ln = len(words[i]), len(words[i+1])
      while j < lc and j < ln and words[i][j] == words[i+1][j]:
        j += 1
      if j < lc and j == ln:
        return ""
      if j < lc and j < ln:
        adj[words[i][j]].add(words[i+1][j])
        
    stack = []
    vis = [False for i in range(26)]
    tempvis = [False for i in range(26)]
    
    def dfs(c):
      x = ord(c)-97
      if tempvis[x]: return False
      if not vis[x]:
        vis[x], tempvis[x] = True, True
        if c in adj:
          for letter in adj[c]:
            if not dfs(letter):
              return False
        stack.append(c)
        tempvis[x] = False
      return True
        
    for c in adj:
      if not dfs(c):
        return ""
      
    res = ""
    while stack:
      res += stack.pop()
    return res