# https://leetcode.com/problems/remove-stones-to-minimize-the-total

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        for p in piles:
            heapq.heappush(h, -p)
        while k > 0:
            x = - heapq.heappop(h)
            x -= math.floor(x/2)
            heapq.heappush(h, -x)
            k -= 1
        return - sum(h)



