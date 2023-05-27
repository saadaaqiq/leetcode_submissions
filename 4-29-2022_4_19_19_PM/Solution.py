# https://leetcode.com/problems/spiral-matrix

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
                
        liste = []
        
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        
        while left < right and top < bottom:
            for j in range(left, right):
                liste.append(matrix[top][j])
            top+=1
            for i in range(top, bottom):
                liste.append(matrix[i][right-1])
            right-=1
            
            if not (left < right and top < bottom):
                break
            
            for j in range(right-1, left-1, -1):
                liste.append(matrix[bottom-1][j])
            bottom-=1
            
            for i in range(bottom-1, top-1, -1):
                liste.append(matrix[i][left])
            left+=1
        
        return liste