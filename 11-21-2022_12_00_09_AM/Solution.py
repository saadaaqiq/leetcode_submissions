# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: 
            return 0
        res = 1
        sign = True if n >= 0 else False
        n = abs(n)
        for i in range(32):
            if (n >> i) & 1:
                p = x
                for j in range(i):
                    p *= p
                res *= p
        return res if sign else 1/res