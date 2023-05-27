# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negs = 0
        n = len(grid[0])
        for row in grid:
            l, r = 0, n
            while l<r:
                mid = (l+r)//2
                if row[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid
            negs += n - l
        return negs