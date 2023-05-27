# https://leetcode.com/problems/house-robber-ii

class Solution:
  def rob(self, nums: List[int]) -> int:
    
    def robbing(houses):
      last, beforelast = 0, 0
      for money in houses:
        temp = max(money + beforelast, last)
        beforelast = last
        last = temp
      return last
    
    if len(nums) <= 3:
      return max(nums)
    return max( robbing( nums[1:] ) , robbing( nums[:len(nums)-1] ) )