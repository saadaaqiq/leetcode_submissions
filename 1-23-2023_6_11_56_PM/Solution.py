# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        s = sum(arr[:n-k])

        mini = s

        for i in range(k):
            s -= arr[i]
            s += arr[i+n-k]
            mini = min(s, mini)

        return sum(arr) - mini

         
