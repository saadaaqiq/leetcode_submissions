# https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = collections.defaultdict(list)
        for source, destination, price in flights:
            adj[source].append((destination, price))
        heap = [(0, 0, src)]
        visited = set()
        res = math.inf
        while heap:
            cost, steps, city = heapq.heappop(heap)
            if steps > k + 1 or (city, steps) in visited:
                continue
            if city == dst:
                res = min(res, cost)
            visited.add((city, steps))
            for d, p in adj[city]:
                heapq.heappush(heap, (cost + p, steps + 1, d))
        return -1 if res > 10000000 else res