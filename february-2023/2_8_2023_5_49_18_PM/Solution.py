# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * (n-1) + [0]
        for i in range(n-2, -1, -1):
            dp[i] = 1 + min([dp[j] for j in range(i, min(n, i + nums[i] + 1))])
        return dp[0]