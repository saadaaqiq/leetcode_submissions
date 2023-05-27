# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        acc = 0
        while num:
            x = num%10
            num = num//10
            if x + acc < 10:
                acc += x
            else:
                acc = (acc + x)//10 + (acc + x)%10
        return acc
