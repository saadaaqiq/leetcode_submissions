# https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        arr = []
        for x in nums:
            arr.append(arr[-1]-x if arr else s - x)
        tab = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            tab[i] = tab[i+1] - nums[i] if i+1<len(nums) else s - nums[i]
        for i in range(len(nums)):
            if arr[i] == tab[i]:
                return i
        return -1