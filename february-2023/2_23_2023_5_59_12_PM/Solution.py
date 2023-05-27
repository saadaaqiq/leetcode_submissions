# https://leetcode.com/problems/ipo

class Solution:
    def findMaximizedCapital(self, k, w, P, C):
        max_heap = []
        min_heap = [(c,p) for c,p in zip(C, P)]
        heapq.heapify(min_heap)
        for i in range(k):
            while min_heap and min_heap[0][0] <= w:
                heapq.heappush(max_heap, -heapq.heappop(min_heap)[1])
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)
        return w