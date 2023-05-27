# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        curr = []

        def comb(i): 
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i>n:
                return
            for j in range(i,n+1):
                curr.append(j)
                comb(j+1)
                curr.pop()
            return

        comb(1)

        return res