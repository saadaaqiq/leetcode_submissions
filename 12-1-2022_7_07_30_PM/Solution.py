# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        c = 1
        for i in range(n-2, -1, -1):
            if c - nums[i] <= 0:
                c = 0
            c += 1
        return c==1