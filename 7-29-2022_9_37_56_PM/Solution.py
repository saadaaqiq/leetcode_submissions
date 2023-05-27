# https://leetcode.com/problems/happy-number

class Solution:
  
  def isHappy(self, n: int) -> bool:
    
    visited = set()
    
    def transform(k):      
      s = sum([ (k//10**i%10)**2 for i in range(int(log10(k))+1) ])
      if s == 1:
        return True
      if s in visited:
        return False
      visited.add(s)
      return transform(s)
    
    
    return transform(n)
    
    
    