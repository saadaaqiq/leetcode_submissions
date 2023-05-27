# https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        prev = 0
        while i < n:
            j = 0
            while i + j < n and s[i+j] == s[i]:
                j += 1
            res += min(prev, j)
            prev = j
            i += j
        return res