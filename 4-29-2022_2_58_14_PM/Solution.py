# https://leetcode.com/problems/spiral-matrix

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
                
        liste = []
        
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        
        while left < right:
            
            if top == bottom or left == right:
                break
            
            for j in range(left, right):
                liste.append(matrix[top][j])
            top+=1
            
            if top == bottom or left == right:
                break
            
            for i in range(top, bottom):
                liste.append(matrix[i][right-1])
            right-=1
            
            if top == bottom or left == right:
                break
            
            for j in reversed(range(left, right)):
                liste.append(matrix[bottom-1][j])
            bottom-=1
            
            if top == bottom or left == right:
                break
            
            for i in reversed(range(top, bottom)):
                liste.append(matrix[i][left])
            left+=1
        
        return liste