# https://leetcode.com/problems/range-addition

class Solution:
  def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    res = [0] * (length + 1)
    for update in updates:
      res[update[0]] += update[2]
      res[update[1]+1] -= update[2]
    for i in range(1, len(res)-1):
      res[i] += res[i-1]
    res.pop()
    return res