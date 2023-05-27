# https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adj = collections.defaultdict(list)
        for x, y in tickets:
            adj[x].append(y)
        for x in adj:
            adj[x].sort()

        counter = {}
        for source in adj:
            for destination in adj[source]:
                if (source, destination) not in counter:
                    counter[(source, destination)] = 0
                counter[(source, destination)] += 1

        curr = []

        def backtrack(source):
            nonlocal res
            curr.append(source)
            if len(curr) == len(tickets) + 1:
                res = curr.copy()
                return True
            for i in range(len(adj[source])):
                destination = adj[source][i]
                if counter[(source, destination)] > 0:
                    counter[(source, destination)] -= 1
                    if backtrack(destination):
                        return True
                    counter[(source, destination)] += 1                    
            curr.pop()
            return False

        backtrack("JFK")   
        return res
