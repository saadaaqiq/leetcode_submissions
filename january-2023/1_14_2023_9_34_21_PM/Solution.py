# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n-2):
          j, k = i+1, n-1
          while j < k:
            if nums[k] + nums[i] > - nums[j]:
              k = bisect_left(nums, nums[k]) if nums[k] == nums[k-1] else k - 1
            elif nums[k] + nums[i] < - nums[j]:
              j = bisect_right(nums, nums[j]) if nums[j] == nums[j+1] else j + 1
            else:
              res.add(tuple([nums[i], nums[j], nums[k]]))
              j += 1
        return res