# https://leetcode.com/problems/spiral-matrix

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        lis = matrix.pop(0)
        
        l = self.spiralOrder([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])-1,-1,-1)]) if matrix else []
        
        return lis + l
        
        
        
                
            
                
                
                
                
                
                
                