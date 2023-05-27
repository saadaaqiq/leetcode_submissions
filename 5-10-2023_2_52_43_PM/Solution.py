# https://leetcode.com/problems/spiral-matrix-ii

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        move = [(0,1), (1,0), (0,-1), (-1,0)]

        def helper(i, j, d, v):
            mat[i][j] = v
            di, dj = move[d]
            if 0 <= i + di < n and 0 <= j + dj < n and mat[i+di][j+dj] == 0:
                helper(i+di, j+dj, d, v+1)
            else:
                dx, dy = move[(d+1)%4]
                if not (0<=i+dx<n and 0<=j+dy<n) or mat[i+dx][j+dy] != 0:
                    return
                helper(i+dx, j+dy, (d+1)%4, v+1)
        
        helper(0, 0, 0, 1)

        return mat