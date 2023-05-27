# https://leetcode.com/problems/reshape-the-matrix

class Solution:
  def matrixReshape(self, mat, r, c):
    if r*c != len(mat)*len(mat[0]):
      return mat
    res = [[]]
    for i in range(len(mat)):
      for j in range(len(mat[0])):
        if len(res[-1]) == c:
          res.append([mat[i][j]])
        else:
          res[-1].append(mat[i][j])
    return res