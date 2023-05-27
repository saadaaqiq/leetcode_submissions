# https://leetcode.com/problems/toeplitz-matrix

class Solution:
  def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
    m, n = len(mat), len(mat[0])
    
    def isDiag(r,c,matrix):
      a, b = r, c
      while a < len(matrix) and b < len(matrix[0]):
        if matrix[a][b] != matrix[r][c]:
          return False
        a += 1
        b += 1
      return True
        
    for j in range(n):
      if not isDiag(0,j,mat): 
        return False
    for i in range(1,m):
      if not isDiag(i,0,mat): 
        return False
  
    return True