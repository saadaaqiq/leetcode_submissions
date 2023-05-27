# https://leetcode.com/problems/course-schedule-ii

class Solution:
  def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
    d = {i:[] for i in range(n)}
    state = [0 for i in range(n)]
    for a, b in pre: 
      d[b].append(a)
    res = []
    def dfs(p):
      if state[p] == 1: 
        return False
      if state[p] == 2: 
        return True
      state[p] = 1
      for q in d[p]: 
        if not dfs(q): 
          return False
      state[p] = 2
      res.append(p)
      return True
    for i in range(n): 
      if not dfs(i): 
        return []
    return list(reversed(res))
    