# https://leetcode.com/problems/majority-element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    dic = {}
    for num in nums:
      dic[num] = 1 if num not in dic else dic[num] + 1
    resk, resv = nums[0], dic[nums[0]]
    for k in dic:
      (resv, resk) = (dic[k], k) if dic[k] > resv else (resv, resk)
    return resk