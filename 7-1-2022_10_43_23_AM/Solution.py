# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
  def twoSum(self, nums: List[int], x: int) -> List[int]:
    
    i, j = 0, len(nums) - 1
    
    while nums[i] + nums[j] != x:
      if nums[i] + nums[j] < x:
        i += 1
      else:
        j -= 1
    
    return i+1,j+1