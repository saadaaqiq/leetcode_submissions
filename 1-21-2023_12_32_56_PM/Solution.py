# https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left_counter = Counter()
        right_counter = Counter(s)
        res = right_counter["0"]
        for c in s:
            left_counter[c] += 1
            right_counter[c] -= 1
            res = min(res, left_counter["1"] + right_counter["0"])
        return res