# https://leetcode.com/problems/naming-a-company

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = {}
        lookup = {}
        for i, w in enumerate(ideas):
            if w[1:] not in lookup:
                lookup[w[1:]] = i
                dic[i] = set() 
            dic[lookup[w[1:]]].add(w[0])
        res = 0
        hm = {chr(i+97): set() for i in range(26)}
        for w in ideas:
            hm[w[0]].add(lookup[w[1:]])
        for a in hm:
            for b in hm:
                if a != b:
                    x, y = 0, 0
                    for i in hm[a]:
                        if i not in hm[b]:
                            x += 1
                    for j in hm[b]:
                        if j not in hm[a]:
                            y += 1
                    res += x * y
                        

        return res