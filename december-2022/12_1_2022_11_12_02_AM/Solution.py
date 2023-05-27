# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0: return a
        elif n == 1: return b
        elif n == 2: return c
        k = 3
        while k <= n:
            d = a + b + c
            a, b, c = b, c, d
            k += 1
        return c