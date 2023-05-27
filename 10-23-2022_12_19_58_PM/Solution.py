# https://leetcode.com/problems/fibonacci-number

class Solution:
  def fib(self, n: int) -> int:
    i,j = 0,1
    for ind in range(2,n+1):
      t = j
      j = i + j
      i = t
    return j if n > 1 else n
      