# https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        replaced = False
        maxi = -100001
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if replaced:
                    return False
                else:
                    if nums[i+1] >= maxi:
                        nums[i] = max(maxi, nums[i+1])
                    else:
                        nums[i+1] = max(maxi, nums[i])
                    replaced = True
            maxi = max(nums[i], maxi)
        return True