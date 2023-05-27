# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = [0] * 3
        for num in nums:
            arr[2-num] += 1
        for i in range(len(nums)):
            while arr[-1] == 0:
                arr.pop()
            nums[i] = 3 - len(arr)
            arr[-1] -= 1
        



