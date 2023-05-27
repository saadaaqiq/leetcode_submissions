# https://leetcode.com/problems/restore-the-array

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n-1, -1, -1):
            x = 0
            for j in range(i, n):
                x = x * 10 + int(s[j])
                if x < 1 or x > k:
                    break
                dp[i] += dp[j+1]

        return dp[0] % (10**9 + 7)










