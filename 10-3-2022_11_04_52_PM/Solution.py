# https://leetcode.com/problems/sparse-matrix-multiplication

class Solution:
  def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    return [ [sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A)) ]
