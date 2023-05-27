# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:
    if n <= 2: 
      return n
    MOD =1_000_000_007
    a, b, c = 1, 1, 2
    for i in range(n-2):
      a, b, c = b, c, (2*c+a)%MOD
    return c
      

