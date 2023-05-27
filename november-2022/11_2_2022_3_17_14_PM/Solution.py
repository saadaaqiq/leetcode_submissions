# https://leetcode.com/problems/minimum-genetic-mutation

class Solution:
  def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    adj = {s: set() for s in (bank+[start])}
    
    def distance(a, b):
      r = 0
      for i in range(8):
        if a[i] != b[i]:
          r += 1
      return r
    
    for s in (bank+[start]):
      for t in (bank):
        if s != t and distance(s,t)==1: 
          adj[s].add(t)
    
    vis = set()    
    
    def dfs(s, d):    
      if s == end:
        return d
      vis.add(s)
      m = 1000
      for t in adj[s]:
        if t not in vis:
          nd = dfs(t, d+1)
          if nd >= 0:
            m = min(m, nd)
      vis.remove(s)
      return m if m<1000 else -1
    
    return dfs(start, 0)
    
    
    
      
      
      
      
      
      
      
      
      