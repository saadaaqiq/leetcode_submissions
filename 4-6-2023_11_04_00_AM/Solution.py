# https://leetcode.com/problems/number-of-closed-islands

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()
        islands = []
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis and grid[i][j] == 0:
                    islands.append([])
                    q = collections.deque([(i,j)])
                    while q:
                        x, y = q.popleft()
                        vis.add((x,y))
                        islands[-1].append((x,y))
                        for (r,c) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                            if (r,c) not in vis and 0<=r<m and 0<=c<n and grid[r][c] == 0:
                                q.append((r,c))
        res = 0
        for island in islands:
            res += 1
            for x, y in island:
                if x in [0,m-1] or y in [0,n-1]:
                    res -= 1
                    break
        return res