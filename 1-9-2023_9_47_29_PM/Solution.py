# https://leetcode.com/problems/minimum-costs-using-the-train-line

class Solution:
    def minimumCosts(self, A: List[int], B: List[int], c: int) -> List[int]:
        n = len(A)
        reg, exp = 0, c
        res = []
        for i in range(n):
            new_reg = \
                min(reg + min(A[i], c + B[i]), exp + min(B[i], A[i]))
            new_exp = \
                min(reg + c + min(A[i], B[i]), exp + min(B[i], A[i]+c))
            reg, exp = new_reg, new_exp
            res.append(min(reg, exp))
        return res

            
   