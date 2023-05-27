# https://leetcode.com/problems/best-sightseeing-pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        X = values[0]
        res = -1
        for i in range(1, n):
            Y = values[i] - i
            res = max(res, X + Y)
            X = max(X, values[i] + i)
        return res