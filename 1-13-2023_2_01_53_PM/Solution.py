# https://leetcode.com/problems/longest-path-with-different-adjacent-characters

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for i in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        res = 0

        def dfs(i):
            nonlocal res
            if not children[i]:
                return 1
            arr = []
            for k, j in enumerate(children[i]):
                d_j = dfs(j)
                if s[i] != s[j]:
                    heapq.heappush(arr, (-d_j, j))
            if len(arr)>1:
                a, b = heapq.heappop(arr), heapq.heappop(arr)
                res = max(res, -a[0]+1-b[0])
                return 1 + max(-a[0],-b[0])
            elif len(arr)==1:
                a = heapq.heappop(arr)
                res = max(res, -a[0]+1)
                return 1 + -a[0]
            else:
                return 1
        
        a = dfs(0)
        return max(a, res)
            
            
                    

            





        

