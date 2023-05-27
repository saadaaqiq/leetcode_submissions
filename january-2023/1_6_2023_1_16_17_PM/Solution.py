# https://leetcode.com/problems/max-increase-to-keep-city-skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        max_row = [0]*n
        max_col = [0]*n
        for i in range(n):
            for j in range(n):
                max_row[i] = max(max_row[i], grid[i][j])
        for j in range(n):
            for i in range(n):
                max_col[j] = max(max_col[j], grid[i][j])
        for i in range(n):
            for j in range(n):
                res += min(max_row[i], max_col[j]) - grid[i][j] 
        return res