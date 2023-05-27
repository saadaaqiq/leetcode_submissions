# https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if sorted(word1) == sorted(word2):
            return True
        A, B = list(Counter(word1).values()), list(Counter(word2).values())
        return sorted(A) == sorted(B) and set(word1) == set(word2)
        