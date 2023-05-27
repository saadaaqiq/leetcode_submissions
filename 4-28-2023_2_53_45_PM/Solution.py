# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        x = sum([(2**(n-1-j) if grid[0][j]==1 else 0) for j in range(n)])
        f = sum([2**j for j in range(n)])
        for row in grid:
            y = sum([(2**(n-1-j) if row[j]==1 else 0) for j in range(n)])
            if x == y or x + y == f:
                continue
            return False
        return True
