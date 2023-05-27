# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:
    if n <= 2: 
      return n
    MOD =1_000_000_007
    f = [0] * (n-2) + [2, 1]
    p = [0] * (n-2) + [1]
    for i in range(n-3, -1, -1):
      f[i] = (f[i+1] + f[i+2] + 2*p[i+1]) % MOD
      p[i] = (p[i+1] + f[i+2]) % MOD
    return f[0] % MOD


      

