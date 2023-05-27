# https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        tree = {}
        for i in range(n):
            l1,r1 = i, i
            while 0<=l1<=r1<n and s[l1]==s[r1]:
                if l1 not in tree:
                    tree[l1] = set()
                tree[l1].add(r1+1)    
                l1-=1
                r1+=1
            l2, r2 = i, i+1
            while 0<=l2<r2<n and s[l2]==s[r2]:
                if l2 not in tree:
                    tree[l2] = set()
                tree[l2].add(r2+1)
                l2-=1
                r2+=1
        def dfs(i):
            res = []
            if i not in tree:
                return [[""]]
            for j in tree[i]:
                for B in dfs(j):
                    arr = [s[i:j]]
                    for t in B:
                        if t:
                            arr.append(t)
                    res.append(arr)
            return res
        
        return dfs(0)
