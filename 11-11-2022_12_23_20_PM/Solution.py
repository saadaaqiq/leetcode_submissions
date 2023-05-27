# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    s = set([nums[0]])
    for j in range(1, len(nums)):
      if nums[j] not in s:
        nums[i] = nums[j]
        s.add(nums[j])
        i += 1
    return len(s)
    
        
