# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:
    if n <= 2:
      return n
    MOD =1_000_000_007
    # matrix exponentiation
    C = [[1,1,2], [1,0,0], [0,1,1]]
    M = [2,1,1]
    def mult(A, B):
      return [\
              (A[0][0]*B[0]+A[0][1]*B[1]+A[0][2]*B[2])%MOD,\
              (A[1][0]*B[0]+A[1][1]*B[1]+A[1][2]*B[2])%MOD,\
              (A[2][0]*B[0]+A[2][1]*B[1]+A[2][2]*B[2])%MOD\
      ]
    
    for i in range(n-2):
      M = mult(C,M)
    
    return M[0]%MOD

      

