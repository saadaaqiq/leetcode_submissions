# https://leetcode.com/problems/paint-fence

class Solution:
  def numWays(self, n: int, k: int) -> int:
    
    if n == 0:
      return 0 
    if n == 1:
      return k
    
    same = k
    diff = k * (k-1)
    
    i = 3
    
    while i <= n:
      temp = diff
      diff = (same + diff) * (k-1)
      same = temp
      i += 1
    
    return same + diff