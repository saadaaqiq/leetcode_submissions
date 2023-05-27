# https://leetcode.com/problems/palindromic-substrings

class Solution:
    
    def countSubstrings(self, s: str) -> int:
        c1=0
        c2=0
        for i in range(len(s)):
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c1+=1
                l-=1
                r+=1
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c2+=1
                l-=1
                r+=1
            
        return c1+c2
            