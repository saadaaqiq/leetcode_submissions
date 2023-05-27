# https://leetcode.com/problems/armstrong-number

class Solution:
  def isArmstrong(self, n: int) -> bool:
    s = 0
    k = 1
    while n // (10**k) >= 1:
      k += 1
    m = n
    while m > 0:
      p = m % 10
      m -= p
      m /= 10
      s += p**k
    return s == n