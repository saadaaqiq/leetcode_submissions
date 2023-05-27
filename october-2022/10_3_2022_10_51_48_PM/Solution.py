# https://leetcode.com/problems/sparse-matrix-multiplication

class Solution:
  def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    res = [ [0 for j in range(len(mat2[0]))] for i in range(len(mat1)) ]
    for i in range(len(mat1)):
      for j in range(len(mat2[0])):
        res[i][j] = sum([mat1[i][k] * mat2[k][j] for k in range(len(mat1[0]))])
    return res