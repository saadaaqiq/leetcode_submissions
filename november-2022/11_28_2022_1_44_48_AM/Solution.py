# https://leetcode.com/problems/wiggle-sort

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if i % 2 != 0:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        
            