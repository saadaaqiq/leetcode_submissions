# https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, arr: List[int]) -> int:
        
        if len(arr) == 1: return arr[0]

        def robbin(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            dp = [0] * (n+2)
            for i in range(n):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[n-1]

        return max(robbin(arr[1:]), robbin(arr[:-1]))
        