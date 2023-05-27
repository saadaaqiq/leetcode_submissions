# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            x = i
            s = 0
            while x:
                if x & 1 == 1:
                    s += 1
                x >>= 1
            res.append(s)
        return res