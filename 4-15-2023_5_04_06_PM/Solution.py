# https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        i = 0
        res = []
        while i < len(s):
            c = s[i]
            k = 0
            while i < len(s) and s[i] == c:
                k += 1
                i += 1
            res.append(str(k) + c)
        return "".join(res)
            
        