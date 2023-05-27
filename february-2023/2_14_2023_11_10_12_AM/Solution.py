# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital

class Solution:
    def minimumFuelCost(self, roads, s):

        adj = collections.defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        
        res = 0

        def dfs(x, p):
            nonlocal res
            passengers = 1 if x > 0 else 0
            for y in adj[x]:
                if y != p:
                    passengers += dfs(y, x)
            if x > 0:
                res += math.ceil(passengers/s)
            return passengers

        dfs(0, -1)

        return res