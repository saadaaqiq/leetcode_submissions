# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [math.inf] * (n-1) + [0]
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                continue
            dp[i] = 1 + min([dp[k] for k in range(i+1, min(i+nums[i]+1, n))])
        return dp[0]
