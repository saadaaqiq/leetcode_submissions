# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
  def myAtoi(self, s: str) -> int:
    res = ''
    i = 0
    while i < len(s) and s[i] == ' ':
      i+=1
    
    if i == len(s): 
      return 0
    
    if s[i] == '-':
      res += '-'
      i+=1
    elif s[i] == '+':
      res += '+'
      i+=1

    if i == len(s) or not (ord(s[i]) <= 57 and ord(s[i])>=48):
      return 0
    
    while i < len(s) and (ord(s[i]) <= 57 and ord(s[i])>=48):
      res += s[i]
      i+=1
      
    res = int(res)
    if res > 2147483647:
      return 2147483647
    if res < -2147483648:
      return -2147483648
    return res