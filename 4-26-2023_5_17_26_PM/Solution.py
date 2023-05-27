# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n
        # 2 3 4 5 1
        # 5 1 2 3 4
        # 4 5 1 2 3
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[n-1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]