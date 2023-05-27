# https://leetcode.com/problems/excel-sheet-column-title

class Solution:
  def convertToTitle(self, col: int) -> str:
    arr = [0,0,0,0,0,0,0]
    n = col
    res = ""
    for i in range(6, -1, -1):
      if n // 26**i > 0:
        arr[i] = (n//26**i)
        
        n -= (n//26**i) * 26**i
    
    for i in range(5):
      if arr[i]==0 and arr[i+1]>0:
        arr[i] += 26
        arr[i+1] -= 1
    while arr:
      p = arr.pop()
      res += chr(64+p) if p > 0 else ""
    return res
    
    
    