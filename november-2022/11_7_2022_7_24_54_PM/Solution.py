# https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            res.append([0 for j in range(i+1)])
        for i in range(1, len(res)):
            for j in range(len(res[i])):
                a = res[i-1][j-1] if j > 0 else 0
                b = res[i-1][j] if j < len(res[i-1]) else 0
                res[i][j] = a + b
        return res