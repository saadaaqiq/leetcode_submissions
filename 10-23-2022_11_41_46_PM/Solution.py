# https://leetcode.com/problems/excel-sheet-column-number

class Solution:
  def titleToNumber(self, col: str) -> int:
    res = 0
    n = len(col)
    for i in range(n):
      res += (ord(col[i])-64) * 26**(n-i-1)
    return res