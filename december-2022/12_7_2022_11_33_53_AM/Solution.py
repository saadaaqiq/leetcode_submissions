# https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if sorted(word1) == sorted(word2):
            return True
        c1, c2 = Counter(word1), Counter(word2)
        A, B = list(c1.values()), list(c2.values())
        return sorted(A) == sorted(B) and set(list(c1.keys())) == set(list(c2.keys()))
        