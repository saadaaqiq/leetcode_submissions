# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
          return 0
        S = set(nums)
        res = 1
        for x in nums:
          if x - 1 in S:
            continue
          else:
            cur = x
            l = 1
            while cur + 1 in S:
              cur = cur + 1
              l += 1
            res = max(res, l)
        return res