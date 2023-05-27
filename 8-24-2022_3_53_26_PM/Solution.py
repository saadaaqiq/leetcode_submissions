# https://leetcode.com/problems/power-of-three

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    return n > 0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 0.00000000000001
