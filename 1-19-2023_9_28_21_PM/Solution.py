# https://leetcode.com/problems/maximum-subarray

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    cs, ms = 0, nums[0]
    for num in nums:
      cs = num + (cs if cs > 0 else 0)
      ms = max(ms, cs)
    return ms