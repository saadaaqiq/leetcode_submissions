# https://leetcode.com/problems/majority-element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    i = 0
    nums.sort()
    while True:
      if nums[i+len(nums)//2] == nums[i]:
        return nums[i]
      i += 1
