# https://leetcode.com/problems/power-of-two

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return n and not n&(n-1)