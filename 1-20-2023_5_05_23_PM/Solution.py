# https://leetcode.com/problems/non-decreasing-subsequences

class Solution:
    def findSubsequences(self, a: List[int]) -> List[List[int]]:
        n = len(a)
        
        def dfs(i):
            if i == n-1:
                return [tuple([]), tuple([a[i]])]
            b = set()
            for j in range(i+1, n):
                if a[j] >= a[i]:
                    for tup in dfs(j):
                        b.add(tup)
                        b.add(tuple([a[i]]+list(tup)))
            return b if b else set([tuple([]), tuple([a[i]])])
        
        res = set()
        for i in range(n):
            for tup in dfs(i):
                res.add(tup)
        
        X = []
        for t in res:
            w = list(t)
            if len(w)>1:
                X.append(w)
        return X