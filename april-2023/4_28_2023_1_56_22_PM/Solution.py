# https://leetcode.com/problems/similar-string-groups

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        par = [i for i in range(n)]
        rank = [0] * n

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            return par[i]
        
        def union(x, y):
            i, j = find(x), find(y)
            if rank[i] > rank[j]:
                par[j] = i
            elif rank[i] < rank[j]:
                par[i] = j
            else:
                par[j] = i
                rank[i] += 1
        
        def diff(a, b):
            c = 0
            for k in range(m):
                if a[k] != b[k]:
                    c += 1
                    if c > 2:
                        return False
            return True

        for i in range(n-1):
            for j in range(i+1, n):
                if diff(strs[i], strs[j]):
                    union(i, j)
        for i in range(n):
            find(i)
        
        return len(set(par))

