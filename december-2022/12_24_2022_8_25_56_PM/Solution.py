# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:
    # bottom up approach: Space optimized
    if n <= 2: return n
    MOD =1_000_000_007
    f, p = [2, 1], [1, 0]
    for i in range(n-3, -1, -1):
      f[1], p[1], f[0], p[0] = f[0], p[0], (f[0] + f[1] + 2*p[0]) % MOD, (p[0] + f[1]) % MOD
    return f[0] % MOD


      

