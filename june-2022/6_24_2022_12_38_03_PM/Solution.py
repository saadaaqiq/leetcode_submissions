# https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    def binarySearch(start_row, end_row, start_column, end_column):
      if start_row >= m or end_row >= m or start_column >= n or end_column >= n or start_row > end_row or start_column > end_column:
        return False
      mid_row = (start_row + end_row) // 2
      mid_column = (start_column + end_column) // 2
      if matrix[mid_row][mid_column] == target:
        return True
      elif matrix[mid_row][mid_column] < target:
        return binarySearch(mid_row+1, end_row, start_column, mid_column) or binarySearch(mid_row+1, end_row, mid_column+1, end_column) or binarySearch(start_row, mid_row, mid_column+1, end_column)
      else:
        return binarySearch(start_row, mid_row-1, start_column, mid_column-1) or binarySearch(start_row, mid_row-1, mid_column, end_column) or binarySearch(mid_row, end_row, start_column, mid_column-1)
    return binarySearch(0, m-1, 0, n-1)