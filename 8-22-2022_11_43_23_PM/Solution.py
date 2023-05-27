# https://leetcode.com/problems/power-of-four

class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    k = 1
    while True:
      if k == n:
        return True
      if k > n:
        return False
      k *= 4