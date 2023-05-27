# https://leetcode.com/problems/last-stone-weight-ii

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = total // 2
        dp = [True] + [False for i in range(target)]
        maxS2 = 0
        for stone in stones:
            temp = dp.copy()
            for somme in range(stone, target + 1):
                if dp[somme-stone]:
                    temp[somme] = True
                    maxS2 = max(maxS2, somme)
                    if maxS2 == target:
                        return total - maxS2 * 2
            dp = temp
        return total - maxS2 * 2


