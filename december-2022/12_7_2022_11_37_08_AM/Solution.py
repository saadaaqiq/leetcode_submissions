# https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        aS, bS = set(word1), set(word2)
        if aS != bS: 
            return False        
        A, B = list(Counter(word1).values()), list(Counter(word2).values())
        return sorted(A) == sorted(B)
        