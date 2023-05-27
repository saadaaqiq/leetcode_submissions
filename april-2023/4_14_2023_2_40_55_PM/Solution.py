# https://leetcode.com/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @cache
        def lps(i, j):
            if i >= j:
                return 1 + j - i
            if s[i] == s[j]:
                return 2 + lps(i+1, j-1)
            else:
                return max(lps(i+1,j), lps(i,j-1))
        
        return lps(0,n-1)