# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num > 0:
            num = num // 2 if num%2==0 else num - 1
            res += 1
        return res