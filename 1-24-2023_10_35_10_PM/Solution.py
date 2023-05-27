# https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adj = collections.defaultdict(list)
        for x, y in tickets:
            adj[x].append(y)
        for x in adj:
            adj[x].sort()

        curr = []
        vis = set()

        def backtrack(source):
            nonlocal res
            curr.append(source)
            if len(curr) == len(tickets) + 1:
                res = curr.copy()
                return True
            for i in range(len(adj[source])):
                destination = adj[source][i]
                adj[source].pop(i)
                if backtrack(destination):
                    return True
                adj[source].insert(i, destination)
            curr.pop()
            return False

        backtrack("JFK")   
        return res
