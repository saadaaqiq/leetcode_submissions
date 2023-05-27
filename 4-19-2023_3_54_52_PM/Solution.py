# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        k = 0
        while k*k <= x:
            k += 1
        return k-1