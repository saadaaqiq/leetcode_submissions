# https://leetcode.com/problems/number-of-zero-filled-subarrays

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                continue
            else:
                j = i
                while j < len(nums) and nums[j] == 0:
                    j += 1
                size = j - i 
                res += (size + 1) * size // 2
                i = j
                
        return res
                