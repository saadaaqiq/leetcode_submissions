# https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        res = 0
        cur, prev = 0, 0
        for i in range(1, n):
            prev, cur = cur, max(cur, arr[i] + prev)
        res = cur
        cur, prev = 0, 0
        for i in range(n-2, -1, -1):
            prev, cur = cur, max(cur, arr[i] + prev)
        return max(res, cur)