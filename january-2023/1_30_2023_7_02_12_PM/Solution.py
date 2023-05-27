# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        C = Counter(blocks[:k])
        res = C["W"]
        for i in range(k, n):
            C[blocks[i]] += 1
            C[blocks[i-k]] -= 1
            res = min(res, C["W"])
        return res