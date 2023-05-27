# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
  
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    m,n = len(matrix), len(matrix[0])
    
    def convertToLinear(i,j):
      return i*n + j

    def convertToCoords(k):
      return (k//n, k%n)
    
    def bs(l, r):
      if l > r:
        False
      else:
        mid = (l+r)//2
        (i,j) = convertToCoords(mid)
        if target == matrix[i][j]:
          return True
        elif target > matrix[i][j]:
          return bs(mid+1,r)
        else:
          return bs(l,mid-1)
    
    return bs(0, convertToLinear(m-1,n-1))