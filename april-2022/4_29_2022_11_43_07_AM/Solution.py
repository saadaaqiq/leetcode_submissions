# https://leetcode.com/problems/rotate-image

def printMat(matrix):
    for elem in matrix:
        print(elem)
    print()
    
class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        k = 0
        n = len(matrix)
        while n - k > k:
            self.subRotate(matrix,k)
            k+=1
            
    def subRotate(self, matrix: List[List[int]], k: int) -> None:
        n = len(matrix)
        
        t = 0
        tlist = matrix[k][k:n-k]
        
        for i in range(k, n-k):
            t = matrix[i][n-k-1]
            matrix[i][n-k-1] = tlist[i-k]
            tlist[i-k] = t
                    
        for j in range(k, n-k):
            t = matrix[n-k-1][n-j-1] if j>k else t
            matrix[n-k-1][n-j-1] = tlist[j-k]
            tlist[j-k] = t
        
        
        for i in range(k, n-k):
            t = matrix[n-i-1][k] if i>k else t
            matrix[n-i-1][k] = tlist[i-k]
            tlist[i-k] = t
        
        for j in range(k, n-k):
            t = matrix[k][j] if j>k else t
            matrix[k][j] = tlist[j-k]
            tlist[j-k] = t
