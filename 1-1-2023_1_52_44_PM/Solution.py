# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.strip().split(" ")
        if len(pattern) != len(arr):
            return False
        d1 = {}
        d2 = {}
        for i,w in enumerate(arr):
            c = pattern[i]
            if c not in d1 and w not in d2:
                d1[c], d2[w] = w, c
            elif c in d1 and d1[c]==w and w in d2 and d2[w]==c:
                continue
            else:
                return False
        return True

            

