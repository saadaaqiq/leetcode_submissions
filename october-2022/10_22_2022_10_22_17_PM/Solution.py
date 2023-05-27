# https://leetcode.com/problems/minimum-window-substring

class Solution:
  def minWindow(self, a, b) -> str:
    if len(b) > len(a): 
      return ""
    ca, cb = {}, {}
    
    for c in b:
      if c not in cb:
        cb[c] = 0
      cb[c] += 1
      
    for c in a:
      if c not in ca:
        ca[c] = 0
      ca[c] += 1
        
    for k in cb:
      if k not in ca or ca[k] < cb[k]:
        return ""
    
    if len(a) == len(b):
      for k in cb:
        if ca[k]!=cb[k]:
          return ""
      return a
    
    for k in ca:
      ca[k] = 0

    i, j, ri, rj = 0, 0, 0, 0

    def isIn(ca,cb):
      for k in cb:
        if ca[k]<cb[k]:
          return False
      return True
        
    while i < len(a):
      if j < len(a):
        if not isIn(ca,cb):
          ca[a[j]] += 1
          j += 1
          if j==len(a) and isIn(ca,cb):
            if j-i < rj-ri or (ri==0 and rj==0): 
              ri, rj = i, j
        else:
          if j-i < rj-ri or (ri==0 and rj==0): 
            ri, rj = i, j
          ca[a[i]] -= 1
          i += 1
      else:
        ca[a[i]] -= 1
        i += 1
        if isIn(ca,cb):
          if j-i < rj-ri or (ri==0 and rj==0): 
            ri, rj = i, j
    
    return "" if rj==0 else a[ri:rj]
      