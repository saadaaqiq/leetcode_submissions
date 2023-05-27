# https://leetcode.com/problems/missing-element-in-sorted-array

class Solution:
  
  def missingElement(self, nums: List[int], k: int) -> int:
    
    left, right = 0, len(nums)
    
    while left < right:
      mid = (left + right) // 2
      if nums[mid] - nums[0] - mid < k:
        left = mid + 1
      else:
        right = mid
    
    return nums[left - 1] + k - nums[left - 1] + nums[0] + left - 1