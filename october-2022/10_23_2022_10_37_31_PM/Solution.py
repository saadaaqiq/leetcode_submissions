# https://leetcode.com/problems/set-mismatch

class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    dic = {i: 0 for i in range(1,len(nums)+1)}
    for n in nums:
      dic[n] += 1
    a, b = 0, 0
    for k in dic:
      if dic[k] == 2:
        b = k
      elif dic[k] == 0:
        a = k
    return [b,a]