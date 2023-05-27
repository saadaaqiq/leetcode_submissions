# https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution:
  def targetIndices(self, nums: List[int], target: int) -> List[int]:
    less = 0 
    tar = 0
    for num in nums:
      if num < target:
        less += 1
      elif num == target:
        tar += 1
    return [i for i in range(less,less+tar)]