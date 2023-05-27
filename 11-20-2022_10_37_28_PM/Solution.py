# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for k in range(3):
            i = 0 
            while i < n and nums[i] <= k:
                i += 1
            j = i
            while j < n:
                if nums[j] == k:
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
                    while i < n and nums[i] <= k:
                        i += 1
                    j = i
                j += 1
        
        

