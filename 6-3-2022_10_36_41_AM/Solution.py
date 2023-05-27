# https://leetcode.com/problems/zigzag-conversion

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = [''] * numRows
    q = deque(s)
    while q:
      i = 0
      while i < numRows - 1 and q:
        rows[i] += q.popleft()
        i+=1
      while i > 0 and q:
        rows[i] += q.popleft()
        i-=1
    res = ''
    for i in range(numRows):
      res += rows[i]
    return res