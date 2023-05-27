# https://leetcode.com/problems/maximum-ice-cream-bars

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        res = 0
        while costs and coins > 0:
            c = heapq.heappop(costs)
            if c <= coins:
                res += 1
                coins -= c
            else:
                break
        return res