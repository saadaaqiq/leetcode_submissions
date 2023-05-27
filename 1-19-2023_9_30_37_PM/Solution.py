# https://leetcode.com/problems/maximum-subarray

class Solution:
  def maxSubArray(self, arr: List[int]) -> int:
    
    def kadanes(nums):
      n = len(nums)
      cs, ms = 0, nums[0]
      for num in nums:
        cs = num + (cs if cs > 0 else 0)
        ms = max(ms, cs)
      return ms

    def sliding_window(nums):
      n = len(nums)
      ml, mr = 0, 0
      cs, ms = 0, nums[0]
      l = 0
      for r in range(n):
        if cs < 0:
          cs = 0
          l = r
        cs += nums[r]
        if cs > ms:
          ms = cs
          ml, mr = l, r
      return ms

    return sliding_window(arr)