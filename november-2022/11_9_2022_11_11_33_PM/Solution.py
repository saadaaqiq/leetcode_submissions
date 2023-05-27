# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mono = []
        profit = 0
        for p in prices:
            m = 0
            while mono and p > mono[-1]:
                m = max(m, p - mono.pop())
            mono.append(p)
            if m < 10000: 
                profit += m
        return profit