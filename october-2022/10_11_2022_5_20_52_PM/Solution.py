# https://leetcode.com/problems/increasing-triplet-subsequence

class Solution:
  
  def increasingTriplet(self, nums: List[int]) -> bool:
    
    i, j = 2**31, 2**31
    
    for ind in range(len(nums)):
      if nums[ind] <= i:
        i = nums[ind]
      elif nums[ind] <= j:
        j = nums[ind]
      else:
        return True
    return False