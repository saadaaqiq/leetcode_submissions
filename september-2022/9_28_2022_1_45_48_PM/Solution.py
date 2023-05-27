# https://leetcode.com/problems/majority-element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    dic = {}
    for num in nums:
      if num not in dic:
        dic[num] = 0
      dic[num] += 1
    resk, resv = nums[0], dic[nums[0]]
    for k in dic:
      if dic[k] > resv:
        resv = dic[k]
        resk = k
    return resk