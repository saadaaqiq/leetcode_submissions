# https://leetcode.com/problems/lexicographically-smallest-equivalent-string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:


        par = [i for i in range(26)]

        def find(k):
            if par[k]!=k:
                par[k] = find(par[k])
            return par[k]
        
        def union(i, j):
            x, y = find(i), find(j)
            if x <= y:
                par[y] = x
            else:
                par[x] = y

        for i in range(len(s1)):
            a, b = ord(s1[i]) - 97, ord(s2[i]) - 97
            union(a,b)

        for i in range(26):
            find(i)
        
        res = ""
        for c in baseStr:
            res += chr(par[ord(c)-97] + 97)
        return res 