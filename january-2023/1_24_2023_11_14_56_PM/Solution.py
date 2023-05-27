# https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for (x, y), q in zip(edges, succProb):
            adj[x].append((y,q))
            adj[y].append((x,q))
        heap = [(-1, start)]
        vis = set()
        while heap:
            p, node = heapq.heappop(heap)
            if node == end:
                return -p
            if node in vis:
                continue
            vis.add(node)
            if node in adj:
                for neighbor,q in adj[node]:
                    heapq.heappush(heap, (p*q, neighbor))
        return 0
