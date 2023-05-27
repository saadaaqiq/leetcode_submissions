# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums)-1
        for i in range(last_pos-1, -1, -1):
            if nums[i] >= last_pos - i:
                last_pos = i
        return last_pos == 0