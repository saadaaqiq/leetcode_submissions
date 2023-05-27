# https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, arr: List[int]) -> int:

        if len(arr) == 1: 
            return arr[0]

        def robbin(nums: List[int]) -> int:
            n = len(nums)
            prevprev, prev, curr = 0, 0, 0
            for i in range(n):
                curr = max(nums[i] + prevprev, prev)
                prevprev, prev, curr = prev, curr, 0
            return prev

        return max(robbin(arr[1:]), robbin(arr[:-1]))
        