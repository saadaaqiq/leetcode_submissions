# https://leetcode.com/problems/one-edit-distance

class Solution:
  
  def isOneEditDistance(self, s: str, t: str) -> bool:

    i, j = 0, len(s)-1
    l, r = 0, len(t)-1
    
    while j>=0 and r>=0 and s[j]==t[r]:
      j -= 1
      r -= 1
    while i<len(s) and l<len(t) and s[i]==t[l]:
      i += 1
      l += 1
    return (i == j and l == r + 1) or (l == r and i == j + 1) or (i == j and l == r)\
            or (i == l and l == len(t)-1 and j == -1 and r == 0)
    