# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, string: str) -> str:
        s = [c for c in string]
        n = len(s)
        res = s[0]
        for i in range(n):
            j, k = i, i+1
            l = 0
            while j>=0 and k<n and s[j] == s[k]:
                j -= 1
                k += 1
                l += 2
            if l > len(res):
                res = ''.join(s[j+1:k])
        for i in range(n):
            j, k = i, i
            while j>=0 and k<n and s[j] == s[k]:
                j -= 1
                k += 1
            if k-j-1 > len(res):
                res = ''.join(s[j+1:k])
        return res

        
        

