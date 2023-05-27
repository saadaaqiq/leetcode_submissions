# https://leetcode.com/problems/missing-element-in-sorted-array

class Solution:
  def missingElement(self, nums: List[int], k: int) -> int:
    c = 0
    prev = nums[0]
    for i in range(1, len(nums)):
      if nums[i] - prev == 1:
        prev = nums[i]
        continue
      if k - c > nums[i] - prev - 1:
        c += nums[i] - prev - 1
        prev = nums[i]
      else:
        return prev + k - c
    return prev + k - c
    