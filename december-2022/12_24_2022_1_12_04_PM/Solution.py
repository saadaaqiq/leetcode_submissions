# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, n: int) -> int:

        @lru_cache
        def dfs(l, w):
            return w if w<=2 else dfs(0, w-1) + l*dfs(1, w-1) + 2*(1-l)*dfs(1, w-2) + (1-l)*dfs(0,w-2)
        return dfs(0, n) % (10**9 + 7)