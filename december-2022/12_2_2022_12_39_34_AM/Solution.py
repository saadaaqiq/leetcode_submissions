# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        res, l, r = 0, 0, 0
        while r < len(nums)-1: l, r, res = r+1, max([i+nums[i] for i in range(l,r+1)]), res+1
        return res