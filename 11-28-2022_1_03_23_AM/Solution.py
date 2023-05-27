# https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        prev, prevarr = 0, deque()

        for i in range(m):
            for j in range(n):
                s = 0
                s += prevarr[j-1] if j-1>=0 and i>0 else 0
                s += prevarr[j] if i>0 else 0
                s += prevarr[j+1] if j+1<n and i>0 else 0
                s += prev if j>0 else 0
                s += board[i][j+1] if j+1<n else 0
                s += board[i+1][j-1] if i+1<m and j-1>=0 else 0
                s += board[i+1][j] if i+1<m else 0
                s += board[i+1][j+1] if i+1<m and j+1<n else 0
                prev = board[i][j]
                prevarr.append(board[i][j])
                if prev == 1 and (s<2 or s>3) : 
                    board[i][j] = 0
                elif prev==0 and s==3: 
                    board[i][j] = 1
            while len(prevarr)>n:
                prevarr.popleft()


                         
