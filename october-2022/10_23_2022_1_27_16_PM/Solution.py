# https://leetcode.com/problems/power-of-two

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    b = bin(n)
    return Counter(b)["1"] == 1 and b[0]!="-"