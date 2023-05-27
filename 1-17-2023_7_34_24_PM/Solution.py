# https://leetcode.com/problems/number-of-good-paths

class Solution:
    def numberOfGoodPaths(self, vals, edges):
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        dic_values = collections.defaultdict(list)
        for i,v in enumerate(vals):
            dic_values[v].append(i)

        good = 0
        n = len(vals)

        pars = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(x):
            if pars[x] != x:
                pars[x] = find(pars[x])
            return pars[x]

        def union(a, b):
            x, y = find(a), find(b)
            if rank[x] < rank[y]:
                pars[x] = y
            elif rank[y] < rank[x]:
                pars[y] = x
            else:
                pars[y] = x
                rank[x] += 1
            
        for v in sorted(dic_values.keys()):
            for i in dic_values[v]:
                for j in adj[i]:
                    if vals[j] <= v:
                        union(j,i)

            count = collections.defaultdict(int)
            for i in dic_values[v]:
                count[find(i)] += 1
                good += count[find(i)]

        return good

        

