# https://leetcode.com/problems/gray-code

class Solution:
  def grayCode(self, n: int) -> List[int]:
    res = [0]
    temp = []
    for i in range(n):
      for x in res:
        temp.append(x)
      for x in reversed(res):
        temp.append(x|(1<<i))
      res, temp = temp.copy(), []
    return res
