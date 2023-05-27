# https://leetcode.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        n = len(nums)
        stack = []
        for i in range(n):
            mi = nums[i]
            while stack and stack[-1][1] < nums[i]:
                mi = min(mi, stack[-1][2])
                stack.pop()
            if stack and stack[-1][1]>nums[i] and stack[-1][2]<nums[i]:
                return True
            stack.append((i,nums[i],mi))
        return False
        
       
        
