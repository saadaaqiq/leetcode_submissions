# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        dic = {}
        rev = {}
        A = s.split(' ')
        if len(A) != len(p):
            return False
        for i,w in enumerate(A):
            if (p[i] in dic and dic[p[i]] != w) or (w in rev and rev[w] != p[i]):
                return False
            dic[p[i]] = w
            rev[w] = p[i]
        return True