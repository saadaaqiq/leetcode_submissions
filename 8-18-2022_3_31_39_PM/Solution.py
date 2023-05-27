# https://leetcode.com/problems/missing-element-in-sorted-array

class Solution:
  
  def missingElement(self, nums: List[int], k: int) -> int:
    
    l, r = 0, len(nums)
    
    while l < r:
      m = (l + r) // 2
      if nums[m] - nums[0] - m < k:
        l = m + 1
      else:
        r = m
    
    return k + nums[0] + l - 1