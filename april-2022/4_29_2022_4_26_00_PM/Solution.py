# https://leetcode.com/problems/spiral-matrix

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        liste = []
        
        while matrix:
            
            liste += matrix.pop(0)
            
            matrix = (list(zip(*matrix)))[::-1]
            
        return liste
    
    
        