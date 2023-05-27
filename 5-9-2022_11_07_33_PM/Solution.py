# https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        exploredPacific = set()
        exploredAtlantic = set()
        m, n = len(heights), len(heights[0])
        
        def bfs(r,c, explored):
            res = []
            explored.add((r,c))
            q = deque()
            q.append((r,c))
            while q:
                i,j = q.popleft()
                b1 = i-1>=0 and heights[i-1][j]>=heights[i][j]
                b2 = i+1<m and heights[i+1][j]>=heights[i][j]
                b3 = j-1>=0 and heights[i][j-1]>=heights[i][j]
                b4 = j+1<n and heights[i][j+1]>=heights[i][j]
                if not b1 and not b2 and not b3 and not b4:
                    res.append((i,j))
                if b1 and (i-1, j) not in explored:
                    explored.add((i-1,j))
                    q.append((i-1, j))
                if b2 and (i+1, j) not in explored:
                    explored.add((i+1, j))
                    q.append((i+1, j))
                if b3 and (i, j-1) not in explored:
                    explored.add((i, j-1))
                    q.append((i, j-1))
                if b4 and (i, j+1) not in explored:
                    explored.add((i, j+1))
                    q.append((i, j+1))
            return res
        
        for j in range(0,n):
            bfs(0,j, exploredPacific)
            bfs(m-1,j, exploredAtlantic)
        for i in range(0,m):
            bfs(i,0, exploredPacific)
            bfs(i,n-1, exploredAtlantic)
        
        results = []
        for (i,j) in exploredPacific.intersection(exploredAtlantic):
            results.append([i,j])
        return results