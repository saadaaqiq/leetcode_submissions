# https://leetcode.com/problems/redundant-connection

class Solution:
  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
    dic = { k+1 : set() for k in range(len(edges)) }
    
    for i,j in edges:
      dic[i].add(j)
      dic[j].add(i)
    
    visited = set()
    cycle = []
    
    def dfs(i, p):
      visited.add(i)
      cycle.append(i)
      if dic[i]:
        for j in dic[i]:
          if j!=p and j not in visited:
            if not dfs(j,i):
              print()
              return False
          elif j!=p and j in visited:
            del cycle[:cycle.index(j)]
            return False
      cycle.pop()
      return True
      
    dfs(1,0) 
    
    edgesInCycle = set([ (cycle[i],cycle[i+1]) for i in range(-1,len(cycle)-1) ])

    for pos in range(len(edges)-1, -1, -1):
      if (edges[pos][0],edges[pos][1]) in edgesInCycle or (edges[pos][1],edges[pos][0]) in edgesInCycle:
        return edges[pos]