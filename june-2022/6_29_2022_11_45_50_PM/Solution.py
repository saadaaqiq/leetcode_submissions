# https://leetcode.com/problems/maximum-subarray

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    s = 0
    m = -10001
    for num in nums:
      if s <= 0:
        s = 0
      s += num
      m = max(s, m)
    return m
    