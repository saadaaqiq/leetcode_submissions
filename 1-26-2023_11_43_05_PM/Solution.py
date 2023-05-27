# https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = collections.defaultdict(list)
        for source, destination, price in flights:
            adj[source].append((destination, price))
        heap = [(0, 0, src)]
        visited = set()
        dic = {i: 0 for i in range(n)}
        while heap:
            cost, steps, city = heapq.heappop(heap)
            if steps > k + 1:
                continue
            if city in visited:
                if steps >= dic[city]:
                    continue
                else:
                    dic[city] = steps
            else:
                visited.add(city)
                dic[city] = steps
            if city == dst:
                return cost
            for d, p in adj[city]:
                heapq.heappush(heap, (cost + p, steps + 1, d))
            
        return -1