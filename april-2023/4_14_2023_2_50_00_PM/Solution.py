# https://leetcode.com/problems/count-vowel-substrings-of-a-string

class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        n = len(s)
        vows = ['a','e','i','o','u']
        arr = [[]]

        for c in s:
            if c in vows:
                arr[-1].append(c)
            else:
                if arr[-1]:
                    arr.append([])
        
        if not arr[-1]:
            arr.pop()
        
        res = 0

        for tab in arr:
            
            for i in range(len(tab)):
                x = 0
                for j in range(i, len(tab)):
                    x |= 2**vows.index(tab[j])
                    if x == 31:
                        res += 1
        return res            




