# https://leetcode.com/problems/minimum-falling-path-sum-ii

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1: 
            return matrix[0][0]
        curr, prev = 1, 0
        while curr < n:
            (i,x), (j,y) = heapq.nsmallest(2, [(k,v) for (k,v) in enumerate(matrix[prev])], key= lambda x:(x[1],x[0]))
            for k in range(n):
                matrix[curr][k] += x if k!=i else y
            curr += 1
            prev += 1
        return min(matrix[n-1])
        

            
            