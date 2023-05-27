# https://leetcode.com/problems/continuous-subarray-sum

class Solution:
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    dic = {0: -1}
    s = 0
    for i, n in enumerate(nums):
      s += n%k
      r = s%k
      if r not in dic:
        dic[r] = i
      elif i-dic[r]>1:
        return True
    return False