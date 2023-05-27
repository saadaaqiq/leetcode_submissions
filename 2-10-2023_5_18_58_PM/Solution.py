# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()

        l, r = 0, len(nums)-1
        
        left = True
        
        while l<=r:
            if left:
                res.append(nums[l])
                l += 1
                left = False
            else:
                res.append(nums[r])
                r -= 1
                left = True
        
        return res