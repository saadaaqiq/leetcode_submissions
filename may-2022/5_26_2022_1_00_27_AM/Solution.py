# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    dic = {}
    def dfs(i):
      if i in dic:
        return dic[i]
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
    
    for i in range(len(nums)):
      dic[i] = dfs(i)
    return max(dic.values())

    
    