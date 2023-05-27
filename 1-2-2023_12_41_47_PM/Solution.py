# https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s = 0
        for c in word:
            if 65 <= ord(c) <= 90: 
                s += 1
        return (65<=ord(word[0])<=90 and s==1) or (s==len(word)) or s==0