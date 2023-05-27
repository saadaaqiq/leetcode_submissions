# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, n: int) -> int:

        @lru_cache
        def dfs(l, w):
            if w <= 2: 
                return max(0,w)
            else:
                if l:
                    return dfs(False, w-1) + dfs(True, w-1)
                else:
                    return 2*dfs(True, w-2) + dfs(False, w-1) + dfs(False, w-2)

        return dfs(False, n) % (10**9 + 7)