# https://leetcode.com/problems/convert-a-number-to-hexadecimal

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = 4294967296 + num
        arr = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        res = []
        while num:
            res.append(arr[num % 16])
            num = num // 16
        return ''.join(reversed(res))
