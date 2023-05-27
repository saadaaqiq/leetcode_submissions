# https://leetcode.com/problems/parallel-courses

class Solution:
  def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
    dic = {i: [] for i in range(n)}
    for pre, crs in relations:
      dic[pre-1].append(crs-1)
    sems = {i: 0 for i in range(n)}
    state = [0 for i in range(n)]
        
    def dfs(p, sem):
      if state[p] == 1:
        return False
      elif state[p] == 2:
        sems[p] = max(sems[p], sem)
        for q in dic[p]:
          if sem+1>sems[q]:
            dfs(q, sem+1)
        return True
      else:
        state[p] = 1
        sems[p] = max(sems[p], sem)
        for q in dic[p]:
          if not dfs(q, sem+1):
            return False
        state[p] = 2
        return True
      
    for i in range(n):
      if not dfs(i, 1):
        return -1
      
    return max([sems[p] for p in range(n)])