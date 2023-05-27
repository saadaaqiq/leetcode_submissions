# https://leetcode.com/problems/perfect-squares

class Solution:
    dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self.dp
        squares = [k*k for k in range(1, int(sqrt(n))+1)]
        while len(dp) < n+1:
            dpk = n+1
            for s in squares:
                if len(dp) < s:
                    break
                dpk = min(dpk, 1+dp[-s])
            dp.append(dpk)
        return dp[n]