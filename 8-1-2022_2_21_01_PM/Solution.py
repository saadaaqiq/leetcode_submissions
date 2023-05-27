# https://leetcode.com/problems/subsets

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    
    def subsets(arr):
      l = len(arr)
      res = [[], [arr[0]]]
      if l == 1: 
        return res
      for sub in subsets(arr[1:]):
        if sub != []:
          res.append(sub)
          res.append(sub + [arr[0]])
      return res
    
    return subsets(nums)