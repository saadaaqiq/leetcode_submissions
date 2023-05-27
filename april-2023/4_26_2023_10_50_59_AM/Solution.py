# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, x: int) -> int:
        if x == 0:
            return 0
        elif x % 9 == 0:
            return 9
        else:
            return x % 9

        


