# https://leetcode.com/problems/trapping-rain-water

class Solution:
  def trap(self, height: List[int]) -> int:
    l, r = 0, len(height)-1
    maxLeft, maxRight = height[l], height[r]
    res = 0
    while l <= r:
      if maxLeft <= maxRight:
        maxLeft = max(maxLeft, height[l])
        res += max(min(maxLeft, maxRight) - height[l], 0)
        l += 1
      else:
        maxRight = max(maxRight, height[r])
        res += max(min(maxLeft, maxRight) - height[r], 0)
        r -= 1
    return res