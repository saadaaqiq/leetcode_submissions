# https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, arr: List[int]) -> bool:
        s = sum(arr)

        @cache
        def dfs(l, r):
            if l > r:
                return 0
            return max(
                (arr[l] if (r-l)%2 else 0) + dfs(l+1,r),
                dfs(l, r-1) + (arr[r] if (r-l)%2 else 0)
            )
        
        return True
            



