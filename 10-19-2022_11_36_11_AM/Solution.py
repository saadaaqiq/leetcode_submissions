# https://leetcode.com/problems/course-schedule

class Solution:
  def canFinish(self, n: int, pre: List[List[int]]) -> bool:
    
    dic = {i: [] for i in range(n)}
    for a, b in pre:
      dic[b].append(a)
      
    vistemp = set()
    
    def dfs(p):
      if p in vistemp:
        return False
      vistemp.add(p)
      for q in dic[p]:
        if not dfs(q):
          return False
      vistemp.remove(p)
      dic[p] = []
      return True
        
    for i in range(n):
      if not dfs(i):
        return False
      
    return True