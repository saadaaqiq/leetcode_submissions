# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
  def lengthOfLIS(self, nums):
    arr = []
    for num in nums:
      added = False
      for j in range(len(arr)):
        if num <= arr[j]:
          arr[j] = num
          added = True
          break
      if not added:
        arr.append(num)
    return len(arr)
