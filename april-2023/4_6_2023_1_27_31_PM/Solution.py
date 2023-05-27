# https://leetcode.com/problems/number-of-longest-increasing-subsequence

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ways = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    if 1 + dp[j] > dp[i]:
                        ways[i] = ways[j]
                        dp[i] = 1 + dp[j]
                    elif 1 + dp[j] == dp[i]:
                        ways[i] += ways[j]
        m = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == m:
                res += ways[i]
        return res
        