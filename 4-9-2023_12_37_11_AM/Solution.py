# https://leetcode.com/problems/binary-number-with-alternating-bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        while n:
            n >>= 1
            if (n & 1) ^ prev == 0:
                return False
            prev = n & 1
        return True