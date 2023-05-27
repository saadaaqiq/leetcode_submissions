# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, a: int, b: int) -> int:
        
        T31 = 1
        for i in range(31):
            T31 = T31 + T31
        
        if a == - T31 and b == -1:
            return -(a + 1)

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

        return res if not neg else - res