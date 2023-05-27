# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    m = 0
    
    for num in numSet:
      if num-1 not in numSet:
        c=1
        while num+c in numSet:
          c+=1
        m = max(m,c)
    
    return m
        