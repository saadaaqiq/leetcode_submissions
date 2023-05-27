# https://leetcode.com/problems/parallel-courses

class Solution:
  def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
    dic = {i: [] for i in range(n)}
    for pre, crs in relations:
      dic[pre-1].append(crs-1)
    sems =  [0 for i in range(n)]
    state = [False for i in range(n)]
        
    def dfs(p, sem):
      if state[p] == True:
        return False
      else:
        sems[p] = max(sems[p], sem)
        state[p] = True
        for q in dic[p]:
          if sem+1 > sems[q]:
            if not dfs(q, sem+1):
              return False
        state[p] = False
        return True

    for i in range(n):
      if not dfs(i, 1):
        return -1
      
    return max(sems)