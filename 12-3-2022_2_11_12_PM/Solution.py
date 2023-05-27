# https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [[max([grid[r][c] for (r,c) in [(i-1,j-1), (i-1,j), (i-1,j+1), (i, j-1), (i,j), (i,j+1), (i+1,j-1),(i+1,j),(i+1,j+1)]]) for j in range(1,len(grid[0])-1)] for i in range(1,len(grid)-1)]