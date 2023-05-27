# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()
        res = 0

        def bfs(i,j):
            q = collections.deque([(i,j)])
            while q:
                r, c = q.popleft()
                for (x,y) in [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in vis and grid[x][y] == "1":
                        vis.add((x, y))
                        q.append((x, y))        

        for i in range(m):
            for j in range(n):
                if (i,j) in vis:
                    continue
                if grid[i][j] == "1":
                    vis.add((i,j))
                    bfs(i,j)
                    res += 1
        
        return res
        