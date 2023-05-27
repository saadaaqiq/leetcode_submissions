# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:

        cur = num
        while cur > 9:
            cur = sum([int(c) for c in str(cur)])
        return cur 