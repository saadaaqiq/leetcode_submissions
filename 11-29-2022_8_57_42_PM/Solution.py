# https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution:
  def targetIndices(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    l = bisect_left(nums, target)
    r = bisect_right(nums, target)
    return [i for i in range(l,r)]