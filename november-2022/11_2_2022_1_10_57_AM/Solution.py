# https://leetcode.com/problems/two-sum

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {num: i for i, num in enumerate(nums)}
    for j, n in enumerate(nums):
      if target-n in dic and j != dic[target-n]:
        return [j,dic[target-n]]
    return []