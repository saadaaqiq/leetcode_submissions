# https://leetcode.com/problems/word-search

class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(i, j, k):
            
            if k == len(word): 
                return True
            
            if i < 0 or j < 0 or i > ROWS - 1 or j > COLS - 1 or board[i][j] != word[k] or (i,j) in path: 
                return False
            
            path.add((i,j))
            
            result = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            
            path.remove((i,j))
            
            return result
            
            
        for i in range(ROWS):
            
            for j in range(COLS):
                
                if dfs(i,j,0):
                    return True
        
        return False
        
        