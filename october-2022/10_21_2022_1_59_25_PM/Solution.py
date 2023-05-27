# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    d = {}
    for i in range(len(nums)):
      if i > k:
        d.pop(nums[i-k-1])
      if nums[i] in d:
        return True
      else:
        d[nums[i]] = i
    return False
    