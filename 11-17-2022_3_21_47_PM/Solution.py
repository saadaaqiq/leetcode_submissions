# https://leetcode.com/problems/fibonacci-number

class Solution:
  def fib(self, n: int) -> int:
    if n == 0:
      return 0
    arr = [0,1]
    while len(arr) <= n:
      arr.append(arr[-1]+arr[-2])
    return arr[-1]