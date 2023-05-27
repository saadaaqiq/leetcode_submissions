# https://leetcode.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            mini = num
            while stack and stack[-1][0] < num:
                mini = min(mini, stack[-1][1])
                stack.pop()
            if stack and stack[-1][0]>num and stack[-1][1]<num:
                return True
            stack.append((num, mini))
        return False
        
       
        
