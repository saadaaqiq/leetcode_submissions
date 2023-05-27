# https://leetcode.com/problems/count-strictly-increasing-subarrays

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n-1) + [1]
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + 1 if nums[i] < nums[i+1] else 1
        return sum(dp)