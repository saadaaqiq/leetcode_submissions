# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        s = sum(arr[n-k:n])
        res = s
        for i in range(k):
            s += arr[i] - arr[n-k+i]
            res = max(res, s)
        return res