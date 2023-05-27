# https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                j += 1
                res += 1
            k = 0
            while i-k >= 0 and i + k + 1 < n and s[i-k] == s[i+k+1]:
                k += 1 
                res += 1
        return res