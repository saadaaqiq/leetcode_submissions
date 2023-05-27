# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, l, r = len(s), 0, 0
        if n <= 2:
            return s[0] if s[0] != s[-1] else s
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                j += 1
            if 2*j - 1 > r - l:
                l, r = i - j + 1, i + j - 1
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i-j] == s[i+j+1]:
                j += 1
            if 2*j - 1 > r - l:
                l, r = i - j + 1, i + j
        return s[l:r+1]