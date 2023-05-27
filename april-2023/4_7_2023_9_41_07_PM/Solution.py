# https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        for i in range(1, len(nums)):
            arr[i] += arr[i-1]
        return arr