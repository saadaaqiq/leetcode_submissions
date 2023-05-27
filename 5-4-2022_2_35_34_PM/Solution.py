# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
        
    def longestPalindrome(self, s: str) -> str:
        
        string = ""
        stringSize = 0
        size = len(s)
        
        for i in range(size):
            
            l,r = i,i
            
            while l>=0 and r<=size-1 and s[l] == s[r]:
                if  r-l+1 > stringSize:
                    string = s[l:r+1]
                    stringSize = r - l + 1
                l-=1
                r+=1
            
            l,r = i,i+1
            
            while l>=0 and r<=size-1 and s[l] == s[r]:
                if  r-l+1 > stringSize:
                    string = s[l:r+1]
                    stringSize = r - l + 1
                l-=1
                r+=1
                
        return string
                
        