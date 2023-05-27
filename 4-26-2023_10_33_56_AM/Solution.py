# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        acc = -1
        for c in str(num):
            x = int(c)
            if acc < 0:
                acc = x
            elif x + acc < 10:
                acc += x
            else:
                y = acc + x
                acc = int(str(y)[0]) + int(str(y)[1])
        return acc
