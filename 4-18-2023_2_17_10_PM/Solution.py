# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        
        @cache
        def dfs(i, rem):
            if i == n or rem <= 0:
                return 0
            res = dfs(i+1, rem)
            cur = 0
            for j in range(min(rem, len(piles[i]))):
                cur += piles[i][j]
                res = max(res, cur + dfs(i+1, rem-j-1))
            return res

        return dfs(0, k)