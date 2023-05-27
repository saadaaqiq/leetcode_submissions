# https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * (n+2)
        for i in range(n):
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
        return max(dp[n-1], dp[n-2])