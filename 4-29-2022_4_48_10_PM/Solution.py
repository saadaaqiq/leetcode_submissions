# https://leetcode.com/problems/rotate-image

class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        k = 0
        n = len(matrix)
        
        while n - k - 1 > k:
            a = 0
            while a<n-2*k-1:
                t = matrix[k][k+a]
                matrix[k][k+a] = matrix[n-k-1-a][k]
                matrix[n-k-1-a][k] = matrix[n-k-1][n-k-1-a]
                matrix[n-k-1][n-k-1-a] = matrix[k+a][n-k-1]
                matrix[k+a][n-k-1] = t
                a+=1
            k+=1