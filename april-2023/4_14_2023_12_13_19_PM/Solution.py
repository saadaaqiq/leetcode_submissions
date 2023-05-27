# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        for k in c1:
            if c1[k] > 0 and abs(c1[k] - c2[k]) > 3:
                return False
        for k in c2:
            if c2[k] > 0 and abs(c1[k] - c2[k]) > 3:
                return False
        return True
