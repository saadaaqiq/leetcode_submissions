# https://leetcode.com/problems/next-greater-element-ii

class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    res = [-1] * len(nums)
    mono = []
    for i in range(2*len(nums)):
      num = nums[i%len(nums)]
      while mono and num > mono[-1][1]:
        j,v = mono.pop()
        res[j] = num
      mono.append((i%len(nums),num))
    return res
      
      