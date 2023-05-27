# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ii = set()
        jj = set()
        lines = len(matrix)
        columns = len(matrix[0])
        i = 0
        k = lines
        while i < k:
            j = 0
            l = columns
            while j < l:
                if i<lines and j<columns and matrix[i][j] == 0:
                    ii.add(i)
                    jj.add(j)
                    l+=j
                    k+=i
                elif (i in ii) or (j in jj):
                    matrix[i%lines][j%columns] = 0
                j+=1
            i+=1
