# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
          onesRow, zeroesRow = 0, 0
          for j in range(n):
            if grid[i][j] == 1: onesRow += 1
            else: zeroesRow += 1
          for j in range(n):
            res[i][j] += onesRow - zeroesRow
        for j in range(n):
          onesRow, zeroesRow = 0, 0
          for i in range(m):
            if grid[i][j] == 1: onesRow += 1
            else: zeroesRow += 1
          for i in range(m):
            res[i][j] += onesRow - zeroesRow
        return res