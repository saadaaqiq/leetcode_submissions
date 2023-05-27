# https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        n = len(nums)
        dp1, dp2 = [0]*(n+1), [0]*(n+1)
        for i in range(1, n):
            dp1[i+1] = max(dp1[i-1] + nums[i], dp1[i])
        for i in range(n-2, -1, -1):
            dp2[i] = max(dp2[i+2] + nums[i], dp2[i+1])
        return max(dp1[-1], dp2[0])
        
        