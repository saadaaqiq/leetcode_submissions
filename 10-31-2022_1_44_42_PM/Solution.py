# https://leetcode.com/problems/toeplitz-matrix

class Solution:
  def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
            
    for j in range(len(mat[0])):
      r, c = 0, j
      while r < len(mat) and c < len(mat[0]):
        if mat[r][c] != mat[0][j]: return False
        r,c = r+1, c+1
      
    for i in range(1, len(mat)):
      r, c = i, 0
      while r < len(mat) and c < len(mat[0]):
        if mat[r][c] != mat[i][0]: return False
        r,c = r+1, c+1
  
    return True