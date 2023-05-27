# https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for j in range(n)] for i in range(m)]
        for i in range(m): grid[i][n-1] = 1
        for j in range(n): grid[m-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] += grid[i+1][j] + grid[i][j+1]
        return grid[0][0]