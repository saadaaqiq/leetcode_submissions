# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        
        negative = False
        if x == MIN:
            # MIN = -2147483648
            # reversed it gives: - 8463847412 < MIN
            return 0
        if x < 0:
            negative = True
            x = -x

        arr = []
        k = 1
        while x > 0:
            arr.append((x % 10**k)//(10**(k-1)))
            x -= x % 10**k
            k += 1
        k = len(arr) - 1
        res = 0

        for p in arr:
            q = 0
            while q < p:
                if q * 10**k < MAX - res:
                    q += 1
                else:
                    return 0
            res += q * 10**k
            k -= 1

        if negative:
            res = -res

        return res
            

          