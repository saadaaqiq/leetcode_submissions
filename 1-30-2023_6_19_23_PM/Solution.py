# https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, arr: List[int]) -> bool:
        s = sum(arr)

        @cache
        def dfs(l, r):
            if l == r:
                return arr[l]
            return max(arr[l] + dfs(l+1,r), dfs(l, r-1) + arr[r])
        
        return dfs(0, len(arr)-1) > s / 2
            



