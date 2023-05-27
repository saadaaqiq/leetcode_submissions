# https://leetcode.com/problems/restore-the-array

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n-1, -1, -1):
            x = 0
            for j in range(i, n):
                x *= 10
                x += int(s[j])
                if 1 <= x <= k:
                    dp[i] += dp[j+1]
                else:
                    break
        return dp[0] % (10**9 + 7)










