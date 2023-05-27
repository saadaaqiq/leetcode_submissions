# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:
    if n <= 2: 
      return n
    MOD =1_000_000_007
    C = [[1,1,2], [1,0,0], [0,1,1]]

    def mult(A, B):
      R = [[0,0,0], [0,0,0], [0,0,0]]
      for i in range(3):
        for j in range(3):
          for k in range(3):
            R[i][j]  = (R[i][j] + A[i][k]*B[k][j]) % MOD
      return R
    
    @cache
    def expo(p):
      nonlocal C
      if p == 1: 
        return C
      elif p % 2: 
        return mult(expo(p-1), C)
      else: 
        return mult(expo(p//2), expo(p//2))
    
    A = expo(n-2)[0]
    
    return (A[0]*2 + A[1] + A[2]) % MOD

      

