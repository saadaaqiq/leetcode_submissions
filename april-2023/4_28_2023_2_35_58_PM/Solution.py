# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        first = 0
        full = 0
        for j in range(n-1, -1, -1):
            first |= grid[0][j] << (n-1-j)
            full |= 1 << (n-1-j)
        for i in range(1, m):
            r = 0
            for j in range(n-1, -1, -1):
                r |= grid[i][j] << (n-1-j)
            if r ^ first != 0 and r ^ first != full:
                return False
        return True
        