# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    myset = set(nums)
    m = 0
    for n in nums:
      if n - 1 in myset:
        continue
      k, c = n, 1
      while k + 1 in myset: c, k = c + 1, k + 1
      m = max(m, c)
    return m
            
            
            
            
            