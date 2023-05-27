# https://leetcode.com/problems/house-robber

class Solution:
  def rob(self, nums: List[int]) -> int:
    dic, memo = {i:[] for i in range(len(nums))}, {}
    
    for i in range(len(nums)):
      if i + 2 < len(nums):
        dic[i].append(i+2)
      if i + 3 < len(nums):
        dic[i].append(i+3)
      
    def dfs(i):
      if len(dic[i]) == 0:
        return nums[i]
      if i in memo:
        return memo[i]
      n = nums[i] + max([ dfs(j) for j in dic[i] ])
      memo[i] = n
      return n
    
    m = 0
    if len(nums) == 1:
      return dfs(0)
    else:
      return max(dfs(0), dfs(1))
      
      
