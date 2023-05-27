# https://leetcode.com/problems/graph-valid-tree

class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
  
    dic = {k:[] for k in range(n)}
    for i,j in edges:
      dic[i].append(j)
      dic[j].append(i)
      
    vis = set()
    
    def dfs(i, pre):
      if i in vis:
        return False
      vis.add(i)
      for j in dic[i]:
        if j != pre:
          if not dfs(j, i):
            return False
      return True
    
    if not dfs(0, -1):
      return False
    if len(vis) != n:
      return False
      
    return True
      