# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        


        l, r = 0, m*n
        while l < r:
            mid = (l+r)//2
            num = matrix[mid//n][mid%n]
            if num < target:
                l = mid + 1
            elif num > target:
                r = mid
            else:
                return True
        return False