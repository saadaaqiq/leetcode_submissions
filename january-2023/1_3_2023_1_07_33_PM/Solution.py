# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, a: int, b: int) -> int:
        LB, HB = -2**31, 2**31 - 1
        neg = (a<0 and b>0) or (a>0 and b<0)
        divident, divisor = - a if a < 0 else a, - b if b < 0 else b
        
        def binary_div(x, y):
            l, r = 0, 1
            k = 0
            while x >= y:
                l, r = r, r+r
                k = y
                y += y
            return (l,r,k)

        res = 0
        while True:
            l, r, k = binary_div(divident, divisor)
            if l == 0: break
            res += l
            divident -= k
        
        if neg: 
            res = - res

        return max(LB, res) if neg else min(HB, res)