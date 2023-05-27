# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        i = 0
        while i < n-2:
          j, k = i+1, n-1
          while j < k:
            if nums[k] + nums[i] > - nums[j]:
              k = bisect_left(nums, nums[k]) if nums[k] == nums[k-1] else k - 1
            elif nums[k] + nums[i] < - nums[j]:
              j = bisect_right(nums, nums[j]) if nums[j] == nums[j+1] else j + 1
            else:
              res.add(tuple([nums[i], nums[j], nums[k]]))
              j += 1
          i = bisect_right(nums, nums[i]) if nums[i] == nums[i+1] else i + 1 
        return res