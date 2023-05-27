# https://leetcode.com/problems/ipo

class Solution:
    def findMaximizedCapital(self, k, w, P, C):
        heap = []
        stack = []
        n = len(P)
        cur = w
        for i in range(n):
            heapq.heappush(heap, (-P[i], C[i]))
        i = 0
        while i < k:
            if not heap:
                break
            mp, c = heapq.heappop(heap)
            if c <= cur:
                cur -= mp
                while stack:
                    heapq.heappush(heap, stack.pop())
                i += 1
            else:
                stack.append((mp, c))
        
        return cur