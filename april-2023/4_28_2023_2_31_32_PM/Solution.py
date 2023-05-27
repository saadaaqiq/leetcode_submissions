# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if (grid[0][0]==grid[i][0] and grid[0][j]!=grid[i][j]) or (grid[0][0]!=grid[i][0] and grid[0][j]==grid[i][j]):
                    return False
        return True