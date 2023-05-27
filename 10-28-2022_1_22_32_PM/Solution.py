# https://leetcode.com/problems/product-of-array-except-self

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1 for i in range(len(nums))]
    old = nums[0]
    for i in range(1, len(nums)):
      temp = nums[i]
      res[i] = old
      old = temp * old
    old = nums[-1]
    for i in range(len(nums)-2, -1,-1):
      temp = nums[i]
      res[i] *= old
      old = temp * old
    return res