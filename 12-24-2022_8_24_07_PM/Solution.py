# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:
    # bottom up approach: Space optimized
    if n <= 2: 
      return n
    MOD =1_000_000_007
    f = [2, 1]
    p = [1, 0]
    for i in range(n-3, -1, -1):
      f0 = (f[0] + f[1] + 2*p[0]) % MOD
      p0 = (p[0] + f[1]) % MOD
      f[1] = f[0]
      p[1] = p[0]
      f[0] = f0
      p[0] = p0
    return f[0] % MOD


      

