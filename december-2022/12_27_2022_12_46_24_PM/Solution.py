# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: 
            return True
        i = len(nums)-2
        s = 1
        while i >= 0:
            if nums[i] >= s:
                s = 1
            else:
                s += 1
            i -= 1
        return s <= nums[0]