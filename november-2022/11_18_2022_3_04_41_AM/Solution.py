# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sr, er = -1, -1
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid + 1
            elif nums[mid]>target:
                r = mid 
            else:
                if mid > 0 and nums[mid-1]==target:
                    r = mid
                else:
                    sr = mid
                    break
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid + 1
            elif nums[mid]>target:
                r = mid
            else:
                if mid<len(nums)-1 and nums[mid+1]==target:
                    l = mid + 1
                else:
                    er = mid
                    break
        
        return [sr, er]

