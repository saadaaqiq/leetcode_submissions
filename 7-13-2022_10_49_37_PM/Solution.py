# https://leetcode.com/problems/roman-to-integer

class Solution:
  def romanToInt(self, s: str) -> int:
    i = 0
    res = 0
    d = {'V': 5, 'L': 50, 'D': 500, 'M': 1000, 'I': 1, 'X': 10, 'C': 100, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    
    while i < len(s):
      if i+1 < len(s) and s[i]+s[i+1] in d:
        res += d[s[i]+s[i+1]]
        i += 2
      else:
        res += d[s[i]]
        i += 1
        
    return res