# https://leetcode.com/problems/majority-element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    i, nums = 0, sorted(nums)
    while True:
      if nums[i+len(nums)//2] == nums[i]:
        return nums[i]
      i += 1
