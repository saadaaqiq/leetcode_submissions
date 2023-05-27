# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    s = set()
    for i in range(len(nums)):
      if i > k:
        s.remove(nums[i-k-1])
      if nums[i] in s:
        return True
      else:
        s.add(nums[i])
    return False
    