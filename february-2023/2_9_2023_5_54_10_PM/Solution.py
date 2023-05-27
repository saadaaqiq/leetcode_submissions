# https://leetcode.com/problems/naming-a-company

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = {}
        for i, w in enumerate(ideas):
            if w[1:] not in dic:
                dic[w[1:]] = set() 
            dic[w[1:]].add(w[0])
        res = 0
        hm = {chr(i+97): set() for i in range(26)}
        for w in ideas:
            hm[w[0]].add(w[1:])
        for a in hm:
            for b in hm:
                if a != b:
                    x, y = 0, 0
                    for w in hm[a]:
                        if w not in hm[b]:
                            x += 1
                    for w in hm[b]:
                        if w not in hm[a]:
                            y += 1
                    res += x * y
                        
        return res