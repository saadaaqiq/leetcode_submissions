# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1001):
            p = bisect_left(nums, i)
            if len(nums) - p == i:
                return i
        return -1