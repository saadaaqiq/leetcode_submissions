# https://leetcode.com/problems/perfect-squares

class Solution:
    def numSquares(self, n: int) -> int:
        squares = set()
        
        for k in range(1, n+1):
            if sqrt(k) % 1 == 0:
                squares.add(k)

        dp = [0] + [n+1] * n

        for s in squares:
            dp[s] = 1

        for k in range(1, n+1):
            for s in squares:
                if k - s >= 0:
                    dp[k] = min(dp[k], dp[s] + dp[k-s])

        return dp[n] if dp[n] != n+1 else -1

        