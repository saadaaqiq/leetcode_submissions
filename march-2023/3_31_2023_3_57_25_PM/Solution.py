# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, mat: List[List[str]], word: str) -> bool:
        m, n, wl = len(mat), len(mat[0]), len(word)
        vis = set()
        def backtrack(i, j, k):
            if k == wl:
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i,j) in vis:
                return False
            if word[k] == mat[i][j]:
                vis.add((i,j))
                res = backtrack(i+1,j,k+1) or backtrack(i,j+1,k+1) or backtrack(i-1,j,k+1) or backtrack(i,j-1,k+1)
                vis.remove((i,j))
                return res
            else:
                return False
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        return False