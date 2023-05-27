# https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            j, k = i, i
            while j >= 0 and k < n and s[j] == s[k]:
                res += 1
                j -= 1
                k += 1
        for i in range(n):
            j, k = i, i+1
            while j >= 0 and k < n and s[j] == s[k]:
                res += 1
                j -= 1
                k += 1
        return res
