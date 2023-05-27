# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

class Solution:
    def nearestExit(self, maze: List[List[str]], start: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        maze[start[0]][start[1]] = "+"
        q = deque([(start[0],start[1],0)])
        while q:
            i,j,steps = q.popleft()
            if (i!=start[0] or j!=start[1]) and (i==0 or j==0 or i==m-1 or j==n-1):
                return steps
            for (r,c) in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                if 0<=r<m and 0<=c<n and maze[r][c]==".":
                    q.append((r,c,steps+1))
                    maze[r][c] = "+"
        return -1