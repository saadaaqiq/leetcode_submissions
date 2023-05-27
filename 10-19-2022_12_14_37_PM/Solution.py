# https://leetcode.com/problems/course-schedule-ii

class Solution:
  def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
    d = {i:[] for i in range(n)}
    for a, b in pre: d[b].append(a)
    temp, vis, res = set(), set(), []
    def dfs(p):
      if p in temp: return False
      if p in vis: return True
      vis.add(p)
      temp.add(p)
      for q in d[p]: 
        if not dfs(q): 
          return False
      temp.remove(p)
      res.append(p)
      return True
    for i in range(n): 
      if not dfs(i): 
        return []
    return list(reversed(res))
    
      