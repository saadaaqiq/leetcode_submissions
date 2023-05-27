# https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
  def minFlipsMonoIncr(self, s: str) -> int:
    res = 0
    x = 0
    for c in s:
      if c == '0':
        res = min(x, res + 1)
      else:
        x += 1
    return res