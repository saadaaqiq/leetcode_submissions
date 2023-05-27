# https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis = set()
        m, n = len(image), len(image[0])
        base = image[sr][sc]
        q = deque([(sr,sc)])
        while q:
            i, j = q.popleft()
            vis.add((i,j))
            if image[i][j] == base:
                image[i][j] = color
            else:
                continue
            for (r,c) in [(i+1,j), (i-1,j), (i,j+1),(i,j-1)]:
                if 0<=r<m and 0<=c<n and (r,c) not in vis:
                    q.append((r,c))
        return image

