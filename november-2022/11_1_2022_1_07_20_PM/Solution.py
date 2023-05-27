# https://leetcode.com/problems/count-and-say

class Solution:
  def countAndSay(self, n: int) -> str:
    return "1" if n == 1 else self.say(self.countAndSay(n-1))
    
  def say(self, s):
    res, i = "", 0
    while i < len(s):
      j = i
      while j < len(s) and s[j] == s[i]: j += 1
      res += self.countAndSay((j-i)*int(s[i])) if j-i>3 else str(j-i)+s[i]
      i = j
    return res
  