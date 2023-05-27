# https://leetcode.com/problems/zigzag-conversion

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = [''] * numRows
    n = len(s)
    j = 0
    while j < n:
      i = 0
      while i < numRows - 1 and j < n:
        rows[i] += s[j]
        j+=1
        i+=1
      while i > 0 and j < n:
        rows[i] += s[j]
        j+=1
        i-=1
    res = ''
    for i in range(numRows):
      res += rows[i]
    return res