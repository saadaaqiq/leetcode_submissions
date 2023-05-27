# https://leetcode.com/problems/find-subarrays-with-equal-sum

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cnt = Counter([nums[i] + nums[i+1] for i in range(len(nums)-1)])
        for v in cnt.values():
            if v >= 2:
                return True
        return False
        
        