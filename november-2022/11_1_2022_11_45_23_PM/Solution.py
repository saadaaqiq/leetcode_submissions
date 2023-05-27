# https://leetcode.com/problems/find-pivot-index

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    arr = [[0,0] for i in range(len(nums))]
    for i in range(1, len(nums)):
      arr[i][0] = arr[i-1][0] + nums[i-1]
    for i in range(len(nums)-2, -1, -1):
      arr[i][1] = arr[i+1][1] + nums[i+1]
    for i in range(len(arr)):
      if arr[i][0] == arr[i][1]:
        return i
    return -1