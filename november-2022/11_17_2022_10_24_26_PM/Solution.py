# https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        while len(h)>=2:
            s1, s2 = heapq.heappop(h), heapq.heappop(h)
            w = abs(s1-s2)
            if w > 0:
                heapq.heappush(h, -w)
        if h:
            return -heapq.heappop(h)
        else:
            return 0
            