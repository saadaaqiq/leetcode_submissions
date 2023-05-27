# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        curr = []

        def comb(i): 
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i == n+1:
                return
            # include i
            curr.append(i)
            comb(i+1)
            curr.pop()
            # ignore i
            comb(i+1)
            return
        
        comb(1)

        return res