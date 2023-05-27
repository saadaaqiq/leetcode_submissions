# https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        while i < n:
            j, k = 0, 0
            while i + j < n and s[i + j] == s[i]:           j += 1
            while i + j + k < n and s[i + j + k] != s[i]:   k += 1
            i += j
            res += min(j, k)            
        return res
