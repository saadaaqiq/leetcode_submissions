# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        A, B = [0] * n, [0] * n
        m, M = math.inf, -math.inf
        for i in range(n):
            m = min(m, prices[i])
            M = max(M, prices[n-1-i])
            A[i] = m
            B[n-1-i] = M
        return max(max([B[i] - A[i] for i in range(n)]), 0)