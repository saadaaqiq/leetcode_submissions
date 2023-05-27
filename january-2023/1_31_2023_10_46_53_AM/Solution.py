# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        s = sum(arr[:n-k])
        res = s
        for i in range(n-k, n):
            s -= arr[i-n+k]
            s += arr[i]
            res = min(res, s)
        return sum(arr) - res