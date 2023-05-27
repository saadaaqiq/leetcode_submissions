# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        vis = set()
        res = 0
        
        def bfs(r,c):
            q = deque()
            q.append([r,c])
            while q:
                cell = q.popleft()
                i, j = cell[0], cell[1]
                if (i,j) not in vis:
                    vis.add((i,j))
                    if i+1<m and (i+1,j) not in vis and grid[i+1][j]=='1':
                        q.append([i+1,j])
                    if i-1>=0 and (i-1,j) not in vis and grid[i-1][j]=='1':
                        q.append([i-1,j])
                    if j+1<n and (i,j+1) not in vis and grid[i][j+1]=='1':
                        q.append([i,j+1])
                    if j-1>=0 and (i,j-1) not in vis and grid[i][j-1]=='1':
                        q.append([i,j-1])
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in vis:
                    bfs(i,j)
                    res+=1
                    
        return res