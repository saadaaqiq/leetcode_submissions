# https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n-1
        if nums[l] > nums[l+1]:
            return l
        if nums[r] > nums[r-1]:
            return r
        while l <= r:
            m = (l+r)//2
            if 0<m<n-1 and nums[m-1]<nums[m] and nums[m]>nums[m+1]:
                return m
            elif m-1>=0 and nums[m-1]>nums[m]:
                r = m - 1
            elif m+1<n and nums[m]<nums[m+1]:
                l = m + 1
        return -1