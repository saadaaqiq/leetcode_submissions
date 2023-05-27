# https://leetcode.com/problems/roman-to-integer

class Solution:
  def romanToInt(self, s: str) -> int:
    i = 0
    res = 0
    normal = {'V': 5, 'L': 50, 'D': 500, 'M': 1000}
    special = {'I': 1, 'X': 10, 'C': 100}
    while i < len(s):
      if s[i] in normal:
        res += normal[s[i]]
        i += 1
      elif s[i] in special:
        if s[i] == 'I':
          if i+1 < len(s) and s[i+1]=='V':
            res += 4
            i += 2
          elif i+1 < len(s) and s[i+1]=='X':
            res += 9
            i += 2
          else:
            res += 1
            i += 1
        elif s[i] == 'X':
          if i+1 < len(s) and s[i+1]=='L':
            res += 40
            i += 2
          elif i+1 < len(s) and s[i+1]=='C':
            res += 90
            i += 2
          else:
            res += 10
            i += 1
        elif s[i] == 'C':
          if i+1 < len(s) and s[i+1]=='D':
            res += 400
            i += 2
          elif i+1 < len(s) and s[i+1]=='M':
            res += 900
            i += 2
          else:
            res += 100
            i += 1
    return res