# https://leetcode.com/problems/reverse-integer

class Solution:
  
  def reverse(self, x: int) -> int:
    
    def countDigits(y):
      y = abs(y)
      if y < 10:
        return 1
      return 1 + countDigits(y//10)
    
    pos = True
    if x < 0:
      pos = False
      x = abs(x)
    if x <= 9:
      return x
    res = 0
    while x >= 10:
      r = x % 10
      x -= r
      x = x // 10
      l = countDigits(res)
      res = res * 10 + r
    res = res * 10 + x
    if not pos:
      res = -res
    if res > 2147483647 or res < -2147483648:
      return 0
    return res
      