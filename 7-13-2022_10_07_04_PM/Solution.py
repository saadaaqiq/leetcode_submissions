# https://leetcode.com/problems/palindrome-number

class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0: 
      return False
    k = 0
    t = 1
    while x // t >= 1:
      t *= 10
      k += 1
    y = x
    while y != 0:
      if y // 10**(k-1) != y % 10:
        return False
      y -= y % 10
      y -= (y // 10**(k-1))*(10**(k-1))
      y //= 10
      k-=2
    
    return True
    