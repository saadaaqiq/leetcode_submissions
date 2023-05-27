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
              tk = k 
              while tk > j and nums[tk] == nums[k]:
                tk -= 1
              k = tk
            elif nums[k] + nums[i] < - nums[j]:
              tj = j
              while tj < k and nums[tj] == nums[j]:
                tj += 1
              j = tj
            else:
              res.add(tuple([nums[i], nums[j], nums[k]]))
              j += 1
        return res