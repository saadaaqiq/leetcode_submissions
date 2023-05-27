# https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        a, b = 1 if 1<=int(s[n-1])<=9 else 0, 1
        for i in range(n-2, -1, -1):
            k = 0
            if 1 <= int(s[i])<= 9:
                k += a
            if s[i] != "0" and 1 <= int(s[i]+s[i+1]) <= 26:
                k += b
            a, b = k, a
        return a
