# https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask = 0
        for c in allowed:
            mask |= (1 << (ord(c) - 97))
        res = 0
        for word in words:
            for c in word:
                if (1 << (ord(c) - 97)) & mask == 0:
                    break
            else:
                res += 1
        return res