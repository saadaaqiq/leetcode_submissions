# https://leetcode.com/problems/2-keys-keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        div = n-1
        while div >= 1:
            if n % div == 0:
                break
            div -= 1
        return self.minSteps(div) + n//div
        