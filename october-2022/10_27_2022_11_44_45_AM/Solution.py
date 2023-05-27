# https://leetcode.com/problems/number-of-provinces

class Solution:
  def findCircleNum(self, mat: List[List[int]]) -> int:
    
    for i in range(len(mat)):
      mat[i][i] = i
      
    rank = [0]*len(mat)
        
    def find(i):
      if mat[i][i] != i:
        mat[i][i] = find(mat[i][i])
      return mat[i][i]
    
    def union(x,y):
      i,j = find(x), find(y)
      if rank[i]>rank[j]:
        mat[j][j] = i
      elif rank[j]>rank[i]:
        mat[i][i] = j
      else:
        rank[i]+=1
        mat[j][j] = i
            
    for i in range(len(mat)-1):
      for j in range(i+1, len(mat[0])):
        if mat[i][j] == 1:
          union(i,j)
    
    for i in range(len(mat)):
      find(i)
    
    return len(Counter([mat[i][i] for i in range(len(mat))]))