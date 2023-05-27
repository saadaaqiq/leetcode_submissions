# https://leetcode.com/problems/single-number

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    mi, ma = min(nums), max(nums)
    arr = [False] * (ma - mi + 1)
    for num in nums:
      if arr[num - mi]:
        arr[num - mi] = False
      else:
        arr[num - mi] = True
    for i,b in enumerate(arr):
      if b:
        return i + mi