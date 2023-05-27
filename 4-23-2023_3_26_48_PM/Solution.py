# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        @cache
        def lps(i, j):
            if i >= j:
                return 1 + j - i
            if s[i] == s[j]:
                return 2 + lps(i+1, j-1)
            else:
                return max(lps(i+1,j), lps(i,j-1))
        
        return n - lps(0,n-1)