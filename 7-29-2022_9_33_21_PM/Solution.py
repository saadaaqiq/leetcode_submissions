# https://leetcode.com/problems/happy-number

class Solution:
  def isHappy(self, n: int) -> bool:
    visited = set()
    def transform(k):
      s = sum([ int(str(k)[i]) * int(str(k)[i]) for i in range(len(str(k))) ])
      if s == 1:
        return True
      if s in visited:
        return False
      visited.add(s)
      return transform(s)
    return transform(n)
    
    
    