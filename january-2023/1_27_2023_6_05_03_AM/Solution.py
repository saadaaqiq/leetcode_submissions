# https://leetcode.com/problems/count-of-matches-in-tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:

        def step(k):
            return ((k-1)//2, (k-1)//2 + 1) if k%2 else (k//2, k//2)

        p = n
        res = 0
        while True:
            matches, teams = step(p)
            res += matches
            p = teams
            if p == 1:
                return res
        


