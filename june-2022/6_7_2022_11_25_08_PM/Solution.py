# https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
  def diagonalSum(self, mat: List[List[int]]) -> int:
    n = len(mat)
    somme = 0
    for i in range(n):
      somme += mat[i][i] + mat[n-i-1][i]
    r = mat[(n//2)][(n//2)] if n%2 == 1 else 0
    return somme - r