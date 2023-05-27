# https://leetcode.com/problems/rotate-image

def printMat(matrix):
    for elem in matrix:
        print(elem)
    print()
    

class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        k = 0
        n = len(matrix)
        
        while n - k - 1 > k:
            a = 0
            while a<n-2*k-1:
                t0 = matrix[k][k+a]
                t1 = matrix[k+a][n-k-1]
                t2 = matrix[n-k-1][n-k-1-a]
                t3 = matrix[n-k-1-a][k]
                
                matrix[k][k+a] = t3
                matrix[k+a][n-k-1] = t0
                matrix[n-k-1][n-k-1-a] = t1
                matrix[n-k-1-a][k] = t2
                
                a+=1
                printMat(matrix)
            k+=1