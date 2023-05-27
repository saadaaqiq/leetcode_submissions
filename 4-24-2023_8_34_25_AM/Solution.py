# https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        while h:
            y = - heapq.heappop(h)
            if not h:
                return y
            x = - heapq.heappop(h)
            if y - x > 0:
                heapq.heappush(h, x - y)
        return 0