# https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (n>>i) & 1:
                res = res ^ (1<<(32-i-1))
        return res