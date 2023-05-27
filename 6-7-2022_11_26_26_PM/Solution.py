# https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
  def diagonalSum(self, mat: List[List[int]]) -> int:
    somme = 0
    for i in range(len(mat)):
      somme += mat[i][i] + mat[len(mat)-i-1][i]
    return somme - mat[(len(mat)//2)][(len(mat)//2)] if len(mat)%2 == 1 else somme