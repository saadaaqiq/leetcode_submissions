# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        s = [c for c in str(num)]
        res = 1010
        def backtrack(first, second):
            nonlocal res
            res = min(res, int(''.join(first)) + int(''.join(second)))
            if len(second) > 1:
                for i in range(len(second)):
                    backtrack(first + [second[i]], second[:i] + second[i+1:])
                    backtrack(first + [second[i]], second[i+1:] + second[:i])
        for i in range(4):
            backtrack([s[i]], s[:i] + s[i+1:])
        return res
