# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dic = {arr[i]: i for i in range(n)}
        res = 0
        for i in range(n-1):
            for j in range(i+1,n):
                pprev, prev = arr[i], arr[j]
                size = 2
                cur = pprev + prev
                while cur in dic and dic[cur] > dic[prev]:
                    size += 1
                    pprev, prev, cur = prev, cur, prev + cur
                res = max(res, size if size > 2 else 0)
        return res