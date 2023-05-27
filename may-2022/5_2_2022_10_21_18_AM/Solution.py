# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sdic = {}
        tdic = {}
        
        for c in s:
            if c not in sdic:
                sdic[c] = 0
            else:
                sdic[c] += 1
        
        for c in t:
            if c not in tdic:
                tdic[c] = 0
            else:
                tdic[c] += 1
                
        for ks in sdic:
            if ks not in tdic or tdic[ks] != sdic[ks]:
                return False
        for ks in tdic:
            if ks not in sdic or sdic[ks] != tdic[ks]:
                return False
        
        return True