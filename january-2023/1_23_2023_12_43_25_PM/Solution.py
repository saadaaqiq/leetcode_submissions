# https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        key_trusted_by_set = {i: set([j for j in range(1,n+1) if j != i]) for i in range(1,n+1)}
        key_trusts_set = {i: set() for i in range(1, n+1)}

        for a, b in trust:
            if a in key_trusted_by_set[b]:
                key_trusted_by_set[b].remove(a)
            key_trusts_set[a].add(b)

        for k in key_trusted_by_set:
            if not key_trusted_by_set[k] and not key_trusts_set[k]:
                return k
        
        return -1
            
        