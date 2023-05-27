# https://leetcode.com/problems/minimum-costs-using-the-train-line

class Solution:
    def minimumCosts(self, A: List[int], B: List[int], c: int) -> List[int]:
        n = len(A)
        reg, exp = 0, c
        res = []
        for i in range(n):
            reg, exp = min(reg+A[i], reg+c+B[i], exp+A[i], exp+B[i]), min(reg+A[i]+c, reg+c+B[i], exp+B[i], exp+A[i]+c)
            res.append(min(reg, exp))
        return res

            
   