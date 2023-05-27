# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r  = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m + 1 
            else:
                r = m
        x = l

        l, r = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        y = l

        a = x-1 if 0<=x-1<len(nums) and nums[x-1]==target else -1
        b = y if 0<=y<len(nums) and nums[y]==target else -1
        
        a, b = min(a,b), max(a, b)
        if a==-1 or b==-1:
            return [-1, -1]
        else:
            return [a, b]
