# https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            for l,r in [(i,i), (i,i+1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l-=1
                    r+=1
                c += (r-l)//2
        return c