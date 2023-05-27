# https://leetcode.com/problems/two-sum

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {nums[0]: 0}
    for i in range(1, len(nums)):
      if target - nums[i] in dic:
        return [dic[target-nums[i]], i]
      elif nums[i] not in dic:
        dic[nums[i]] = i
    return [0,0]