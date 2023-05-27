# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        l, r = 0, 0
        while r < len(nums):
            if nums[r] - nums[l] <= k:
                r += 1
            else:
                res += 1
                l = r
        return res