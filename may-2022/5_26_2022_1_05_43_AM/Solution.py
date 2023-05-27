# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    dic = {}
    def dfs(i):
      if len(nums[i:]) == 1:
        dic[i] = 1
        return 1
      m = 0
      for j in range(i+1,len(nums)):
        if nums[j] > nums[i]:
          if j not in dic:
            dic[j] = dfs(j)
          m = max(m,dic[j])
      return m + 1
    
    i=len(nums)-1
    m=0
    while i>=0:
      if i not in dic:
        dic[i] = dfs(i)
      m = max(m,dic[i])
      i-=1
    return m

    
    