# https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        C, X = Counter(s), Counter()
        res = C["0"]
        for c in s:
            X[c], C[c] = X[c]+1, C[c]-1
            res = min(res, X["1"] + C["0"])
        return res