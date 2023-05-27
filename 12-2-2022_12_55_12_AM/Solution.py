# https://leetcode.com/problems/maximum-subarray

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    ml, l, n = -float("infinity"), 0, len(nums)
    for i in range(n):
      ml = max(ml, l + nums[i])
      l = max(0, l + nums[i])
    return ml
    