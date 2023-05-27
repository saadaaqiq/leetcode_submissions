# https://leetcode.com/problems/possible-bipartition

class Solution:
  def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    groups = {i:0 for i in range(1,n+1)}
    adj = collections.defaultdict(list)
    for x,y in dislikes:
      adj[x].append(y)
      adj[y].append(x)

    def dfs(i):
      if groups[i] == 0:
        groups[i] = 1
        return dfs(i)
      else:
        for d in adj[i]:
          if groups[d] == groups[i]:
            return False
          elif groups[d] == 0:
            groups[d] = - groups[i]
            if not dfs(d): 
              return False
      return True

    for i in range(1, n+1):
      if not dfs(i):
        return False

    return True

            
      

    