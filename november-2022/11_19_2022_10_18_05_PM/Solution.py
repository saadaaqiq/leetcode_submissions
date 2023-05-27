# https://leetcode.com/problems/number-of-provinces

class Solution:
  def findCircleNum(self, mat: List[List[int]]) -> int:
    n = len(mat)
    par = [i for i in range(n)]
    rank = [0 for i in range(n)]
    
    def find(i):
      if par[i] != i:
        par[i] = find(par[i])
      return par[i]
    
    def union(i,j):
      x, y = find(i), find(j)
      if rank[x]>rank[y]:
        par[y]=x
      elif rank[x]<rank[y]:
        par[x]=y
      else:
        rank[x]+=1
        par[y]=x
    
    for i in range(n-1):
      for j in range(i+1,n):
        if mat[i][j] == 1:
          union(i,j)
    
    for i in range(n):
      find(i)
    
    return len(set(par))
    
