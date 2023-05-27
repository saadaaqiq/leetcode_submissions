# https://leetcode.com/problems/confusing-number

class Solution:
  def confusingNumber(self, n: int) -> bool:
    dic = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8, 2: -1, 3: -1, 4: -1, 5: -1, 7: -1}
    m = n
    i = 1
    k = 0
    l = len(str(m))
    while m != 0:
      r = m%(10**i)
      if dic[(r//(10**(i-1)))]<0:
        return False
      m -= r
      k += dic[(r//(10**(i-1)))]*(10**(l-i))
      i+=1
    return not k == n