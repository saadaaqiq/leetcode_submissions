# https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = set([(0,0)])
        heap = []
        heapq.heappush(heap, (grid[0][0], (0,0)))
        while heap:
            t, (i,j) = heapq.heappop(heap)
            if i == n-1 and j == n-1:
                return t
            for (r,c) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0<=r<n and 0<=c<n and (r,c) not in vis:
                    vis.add((r,c))
                    heapq.heappush(heap, (max(t, grid[r][c]), (r,c)))
        return 0