# https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m,n = len(matrix), len(matrix[0])
    r,c = m-1, 0
    
    while r >= 0 and c < n:
      if matrix[r][c] == target:
        return True
      elif matrix[r][c] > target:
        r -= 1
      else:
        c += 1
    
    return False