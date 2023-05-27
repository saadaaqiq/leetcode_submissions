# https://leetcode.com/problems/2-keys-keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        div = 0
        for k in range(1,n):
            if n % k == 0:
                div = k
        return self.minSteps(div) + 1 + (n//div - 1)
        