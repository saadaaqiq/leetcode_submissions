# https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for k in count:
            while count[k] >= 2:
                count[k] -= 2
                res += 2
        for k in count:
            if count[k] > 0:
                res += 1
                break
        return res