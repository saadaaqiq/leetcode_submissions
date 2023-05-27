# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c = 1
        for i in range(len(nums)-2, -1, -1):
            c = c + 1 if c > nums[i] else 1
        return c==1