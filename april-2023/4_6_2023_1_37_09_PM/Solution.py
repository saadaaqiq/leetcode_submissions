# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]

        def dfs(i,j):
            if dp[i][j] == 1:
                for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0<=i+di<m and 0<=j+dj<n:
                        if matrix[i+di][j+dj] > matrix[i][j]:
                            dp[i][j] = max(dp[i][j], 1 + dfs(i+di,j+dj))
            return dp[i][j]

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        
        return res