# https://leetcode.com/problems/perfect-squares

class Solution:
    def numSquares(self, target: int) -> int:
        squares = [k*k for k in range(1,math.ceil(sqrt(target))+1) if k*k<=target]
        dp = [0] + [math.inf]*target
        res = math.inf
        for square in squares:
            for t in range(1, target+1):
                if t - square < 0:
                    continue
                else:
                    dp[t] = min(dp[t], 1 + dp[t-square])
            res = min(res, dp[-1])
        return res

