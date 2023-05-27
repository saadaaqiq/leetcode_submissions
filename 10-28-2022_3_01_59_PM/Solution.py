# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    m = 0
    numSet = set(nums)
    for n in nums:
      if n-1 not in numSet: 
        c = 0
        while n+c in numSet: c += 1
        m = max(m, c)
    return m