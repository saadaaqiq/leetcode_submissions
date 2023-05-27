# https://leetcode.com/problems/alien-dictionary

class Solution:
  def alienOrder(self, w: List[str]) -> str:
    adj = {w[i][j]: set() for i in range(len(w)) for j in range(len(w[i]))}
    for i in range(len(w)-1):
      j = 0 
      while j < len(w[i]) and j < len(w[i+1]) and w[i][j] == w[i+1][j]:
        j += 1
      if j < len(w[i]) and j == len(w[i+1]):
        return ""
      if j < len(w[i]) and j < len(w[i+1]):
        adj[w[i][j]].add(w[i+1][j])
        
    stack = []
    vis = [False for i in range(26)]
    tempvis = [False for i in range(26)]
    
    def dfs(c):
      if tempvis[ord(c)-97]:
        return False
      if not vis[ord(c)-97]:
        vis[ord(c)-97] = True
        tempvis[ord(c)-97] = True
        if c in adj:
          for letter in adj[c]:
            if not dfs(letter):
              return False
        stack.append(c)
        tempvis[ord(c)-97] = False
      return True
        
    for c in adj:
      if not dfs(c):
        return ""
      
    res = ""
    while stack:
      res += stack.pop()
    return res