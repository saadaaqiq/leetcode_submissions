# https://leetcode.com/problems/spiral-matrix

class Solution:
    
    def getSlice(self, matrix: List[List[int]], side: int) -> List[int]:
        l = []
        if side == 0 and matrix:
            l = matrix.pop(0)
        elif side == 1 and matrix:
            for elem in matrix:
                if elem:
                    l.append(elem.pop(len(elem)-1))
        elif side == 2 and matrix:
            l = matrix.pop(len(matrix)-1)
            l.reverse()
        elif side == 3 and matrix:
            for elem in matrix:
                if elem:
                    l.append(elem.pop(0))
            l.reverse()
        return l
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        l = []
        side = 0
        while matrix:
            
            l += self.getSlice(matrix, side%4)
            side+=1
        
        return l
        
        
        
                
            
                
                
                
                
                
                
                