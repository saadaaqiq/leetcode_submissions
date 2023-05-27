# https://leetcode.com/problems/sort-the-matrix-diagonally

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            arr = []
            r, c = i, 0
            while r < m and c < n:
                arr.append(mat[r][c])
                r += 1
                c += 1
            arr.sort()
            r, c = i, 0
            ind = 0
            while r < m and c < n:
                mat[r][c] = arr[ind]
                ind += 1
                c += 1
                r += 1
        for j in range(1, n):
            arr = []
            r, c = 0, j
            while r < m and c < n:
                arr.append(mat[r][c])
                r += 1
                c += 1
            arr.sort()
            r, c = 0, j
            ind = 0
            while r < m and c < n:
                mat[r][c] = arr[ind]
                ind += 1
                c += 1
                r += 1
        return mat