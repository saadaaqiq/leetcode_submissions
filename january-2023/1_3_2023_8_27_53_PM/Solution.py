# https://leetcode.com/problems/gray-code

class Solution:
  def grayCode(self, n: int) -> List[int]:
    res = []
    for i in range(2**n):
      x = ((i>>i.bit_length())&1)<<i.bit_length()
      for j in range(i.bit_length(), 0, -1):
        x = x|(0<<(j-1)) if (i>>j)&1==(i>>(j-1))&1 else x|(1<<(j-1))
      res.append(x)
    return res