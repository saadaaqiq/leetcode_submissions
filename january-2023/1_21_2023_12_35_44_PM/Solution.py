# https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        l0, l1 = 0, 0
        r0, r1 = 0, 0
        for c in s:
            if c == "0":    r0 += 1
            else:           r1 += 1
        res = r0
        for c in s:
            if c == "0":    
                l0 += 1
                r0 -= 1
            else:
                l1 += 1
                r1 -= 1
            res = min(res, l1 + r0)
        return res

