# https://leetcode.com/problems/house-robber

class Solution:
  def rob(self, nums: List[int]) -> int:
    g, h = 0, 0
    for num in nums:
      t = max(num + g, h)
      g = h
      h = t
    return h