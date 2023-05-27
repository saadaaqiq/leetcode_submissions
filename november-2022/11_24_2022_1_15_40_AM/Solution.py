# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = set()

        def dfs(i, j, k):
            nonlocal m, n
            if board[i][j] != word[k]: return False
            if k == len(word)-1 and board[i][j] == word[k]: return True
            vis.add((i,j))
            for (r,c) in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                if 0<=r<m and 0<=c<n and (r,c) not in vis:
                    if dfs(r,c,k+1):
                        vis.remove((i,j))
                        return True
            vis.remove((i,j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

