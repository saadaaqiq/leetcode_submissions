# https://leetcode.com/problems/course-schedule

class Solution:
  def canFinish(self, n: int, pre: List[List[int]]) -> bool:
    
    dic = {i: set() for i in range(n)}
    for a, b in pre:
      dic[b].add(a)
      
    stack = []
    vistemp = set()
    vis = set()
    
    def dfs(p):
      if p in vistemp:
        return False
      if p in vis:
        return True
      vis.add(p)
      vistemp.add(p)
      for q in dic[p]:
        if not dfs(q):
          return False
      vistemp.remove(p)
      stack.append(p)
      return True
        
    for i in range(n):
      if not dfs(i):
        return False
      
    return len(stack) == n