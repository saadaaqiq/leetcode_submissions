# https://leetcode.com/problems/excel-sheet-column-number

class Solution:
  def titleToNumber(self, col: str) -> int:
    res = 0
    m = 1
    for i in range(len(col)-1, -1, -1):
      res += (ord(col[i])-64) * m
      m *= 26
    return res