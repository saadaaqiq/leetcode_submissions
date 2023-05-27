# https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed_set = set(c for c in allowed)
        for w in words:
            if set(c for c in w) <= allowed_set:
                res += 1
        return res