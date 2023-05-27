# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid

class Solution:
    def minCost(self,s,h,rc,cc):
        res = 0
        i, j = h[0], h[1]
        
        while i != s[0]:
          res += rc[i]
          i += 1 if h[0] < s[0] else -1
          
        
        while j != s[1]:
          res += cc[j]
          j += 1 if h[1] < s[1] else -1
          
        return res
        
        
