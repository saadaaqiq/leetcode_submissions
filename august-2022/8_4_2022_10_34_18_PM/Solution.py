# https://leetcode.com/problems/paint-fence

class Solution:
  def numWays(self, n: int, k: int) -> int:
    
    b, a = k, 0

    for i in range(1,n):
      b, a = (b + a) * (k-1), b

    return a + b