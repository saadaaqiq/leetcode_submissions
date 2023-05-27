# https://leetcode.com/problems/convert-a-number-to-hexadecimal

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 4294967296
        res = []
        while num:
            res.append(str(num%16) if num%16 < 10 else chr(num%16 + 87))
            num = num // 16
        return ''.join(reversed(res))
