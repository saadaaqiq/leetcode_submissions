# https://leetcode.com/problems/power-of-four

class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    i = 0
    while 4**i < n:
      i += 1
    return 4**i == n