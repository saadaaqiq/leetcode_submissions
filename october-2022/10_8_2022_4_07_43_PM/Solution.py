# https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
  def countSegments(self, s: str) -> int:
    res = 0
    space = True
    for c in s:
      if c == " " and not space:
        space = True
      elif c != " " and space:
        res += 1
        space = False
    return res
        