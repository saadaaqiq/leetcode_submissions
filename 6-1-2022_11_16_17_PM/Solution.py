# https://leetcode.com/problems/jump-game

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1:
      return True
    i,j = 0,1
    while j < len(nums):
      if nums[i] == 0:
        return False
      if nums[i] > nums[j]:
        nums[j] = nums[i] - 1
      i = j
      j = j + 1

    return True