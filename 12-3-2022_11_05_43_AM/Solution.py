# https://leetcode.com/problems/two-sum-less-than-k

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -float("infinity")
        l, r = 0, bisect_right(nums, k)-1
        while l < r:
            if nums[l] + nums[r] >= k:
                r -= 1
            else:
                res = max(nums[l]+nums[r], res)
                l += 1
        return res if res >=0 else -1
