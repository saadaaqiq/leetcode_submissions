# https://leetcode.com/problems/paint-fence

class Solution:
  def numWays(self, n: int, k: int) -> int:
    
    result = [0] * n + [1,0,0]
    
    for i in range(n-1, -1, -1):
      a = 0
      p = i
      while p + 1 < n+1:
        a += result[p+1]
        a -= result[p+3]
        p += 3
      result[i] = k * a
      
    return result[0]