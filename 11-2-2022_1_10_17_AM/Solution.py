# https://leetcode.com/problems/maximum-subarray

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    s = 0
    m = -float("infinity")
    for num in nums:
      s = max(s, 0)
      s += num
      m = max(s, m)
    return m