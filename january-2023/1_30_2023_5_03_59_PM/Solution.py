# https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def dfs(l, r, alice, a_s, b_s):
            if r < l:
                return a_s > b_s
            return (alice and (dfs(l+1, r, False, a_s + piles[l], b_s) or dfs(l, r-1, False, a_s + piles[r], b_s))) or (not alice and (dfs(l+1, r, True, a_s, b_s + piles[l]) or dfs(l, r-1, True, a_s, b_s + piles[r])))

        return dfs(0, len(piles)-1, True, 0, 0)

            