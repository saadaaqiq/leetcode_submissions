# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        curr = []

        def comb(i): 
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i > n:
                return
            # do
            curr.append(i)
            comb(i+1)
            curr.pop()
            # don't
            comb(i+1)
            return
        
        for i in range(1,n+1):
            curr.append(i)
            comb(i+1)
            curr.pop()

        return res