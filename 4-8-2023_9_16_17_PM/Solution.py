# https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        x = n
        c = 0
        while x:
            k = x&1
            x >>= 1
            res |= ((1-k)%2 << c)
            c += 1
        return res