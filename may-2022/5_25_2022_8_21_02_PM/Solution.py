# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    
    dic = { index : 0 for index in range(len(nums)) }
    i = len(nums) - 1
    
    while i >= 0:
      m = 0
      for j in range(i, len(nums)):
        if nums[j] > nums[i]:
          m = max(m, dic[j])
      dic[i] = 1 + m
      i-=1
    
    return max(dic.values())