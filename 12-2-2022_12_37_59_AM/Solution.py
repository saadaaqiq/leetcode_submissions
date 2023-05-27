# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        res, n, l, r = 0, len(nums), 0, 0
        while r < n-1:
            nr = 0
            for i in range(l, r+1):
                nr = max(nr, i+nums[i])
            l = r+1
            r = nr
            res += 1
        return res