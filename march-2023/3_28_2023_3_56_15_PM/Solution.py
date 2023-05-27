# https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        s = 0
        for i in range(m):
            s += grid[i][0]
            dp[i][0] = s

        s = 0
        for j in range(n):
            s += grid[0][j]
            dp[0][j] = s

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
