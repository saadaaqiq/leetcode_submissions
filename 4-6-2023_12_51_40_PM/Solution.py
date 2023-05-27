# https://leetcode.com/problems/2-keys-keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                if i % j == 0:
                    dp[i] = i // j + dp[j]
                    break
        return dp[n]