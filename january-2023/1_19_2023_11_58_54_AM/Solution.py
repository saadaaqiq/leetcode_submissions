# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            j = nums[i]-1
            while 0<=j<n and nums[j]!=j+1:
                temp = nums[j]
                nums[j] = j+1
                j = temp-1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
            