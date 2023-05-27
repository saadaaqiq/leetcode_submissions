# https://leetcode.com/problems/gray-code

class Solution:
  def grayCode(self, n: int) -> List[int]:
    res = []
    for i in range(2**n):
      length = i.bit_length()
      leading_bit = (i>>length) & 1
      x = leading_bit << length
      for j in range(length, 0, -1):
        a, b = (i>>j)&1, (i>>(j-1))&1
        x = x|(0<<(j-1)) if a==b else x|(1<<(j-1))
      res.append(x)
    return res