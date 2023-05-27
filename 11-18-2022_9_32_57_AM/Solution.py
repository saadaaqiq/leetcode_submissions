# https://leetcode.com/problems/ugly-number

class Solution:
    def isUgly(self, n: int) -> bool:
        k = n
        while k > 1:
            if k%3==0:
                k /= 3
            elif k%2==0:
                k /= 2
            elif k%5==0:
                k /= 5
            else:
                return False
        return k==1