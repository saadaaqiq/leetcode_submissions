# https://leetcode.com/problems/majority-element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    count, res = 0, 0
    for num in nums:
      if count == 0:
        res, count = num, 1
      elif num == res:
        count += 1
      else:
        count -= 1
    return res