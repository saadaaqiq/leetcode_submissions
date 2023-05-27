# https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {src: [] for src, dst, w in times}
        for src, dst, w in times:
            adj[src].append((dst, w))

        dic = {}

        heap = [(0, k)]
        while heap:
            w, node = heapq.heappop(heap)
            if node in dic:
                continue
            dic[node] = w
            if node in adj:
                for neighbor, cost in adj[node]:
                    heapq.heappush(heap, (cost + w, neighbor))
        
        if len(dic) < n:
            return -1
        else:
            return max(dic.values())