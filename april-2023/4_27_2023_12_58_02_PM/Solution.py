# https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n, res = len(s), 0

        for i in range(n-1):
            if s[i] != s[i+1]:
                l, r = i, i + 1
                while l >= 0 and r < n:
                    if s[l] == s[i] and s[r] == s[i+1]:
                        res += 1
                        l, r = l - 1, r + 1
                    else:
                        break
        return res
                
