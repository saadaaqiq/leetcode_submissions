# https://leetcode.com/problems/number-of-operations-to-make-network-connected

class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if n == 1:
            return 0

        if len(connections) < n-1:
            return -1

        pars = [i for i in range(n)]
        rank = [0] * n
        
        def find(i):
            if pars[i] != i:
                pars[i] = find(pars[i])
            return pars[i]
        
        def union(x, y):
            i, j = find(x), find(y)
            if rank[i] < rank[j]:
                pars[i] = j
            else:
                pars[j] = i
                rank[i] += 1 if rank[i] == rank[j] else 0

        for x, y in connections:
            union(x, y)
        
        for i in range(n):
            find(i)

        return len(set(pars)) - 1



