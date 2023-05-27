# https://leetcode.com/problems/bulb-switcher

class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        x = 1
        while True:
            y = x * x
            if y <= n:
                res += 1
                x += 1
            else:
                return res
