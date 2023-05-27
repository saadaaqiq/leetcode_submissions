# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    myset = set(nums)
    res = 0
    for num in nums:
      if num-1 not in myset:
        k, c = num, 1
        while k + 1 in myset:
          c += 1
          k += 1
        res = max(res, c)
    return res