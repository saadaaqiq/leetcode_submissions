# https://leetcode.com/problems/largest-number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            x, y = int(a+b), int(b+a)
            return x - y
        nums = sorted([str(num) for num in nums], key=cmp_to_key(compare), reverse=True)
        c = 0
        while c < len(nums) and nums[c] == "0":
            c += 1
        if c == len(nums): 
            return "0"
        else: 
            return ''.join(nums[c:])