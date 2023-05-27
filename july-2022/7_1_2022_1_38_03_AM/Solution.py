# https://leetcode.com/problems/jump-game

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    l = len(nums)
    i = l-1
    c = (True, 0)
    while i > 0:
      i -= 1
      if nums[i] == 0:
        if c[0]:
          c = False, 2
        else:
          c = False, c[1] + 1
      else:
        if not c[0]:
          if nums[i] >= c[1]:
            c = True, 0
          else:
            c = False, c[1] + 1
    return c[0]