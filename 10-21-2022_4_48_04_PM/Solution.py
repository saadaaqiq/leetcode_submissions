# https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    """arr = [0]
    for n in nums:
      arr += [n^x for x in arr]
    return sum(arr)"""
    
    def sums(n, i):
      if i == len(nums):
        return n           
      return sums(n,i+1) + sums(n^nums[i],i+1)
    return sums(0, 0)
    
    """
    powerset = [[]]
    for num in nums:
      extension = []
      for sub in powerset:
        extension.append(sub.copy() + [num])
      powerset += extension
    print(powerset)
    """
    
    """
    powerset = []
    for i in range(1 << len(nums)):
      subset = []
      for j in range(len(nums)):
        if i & (1 << j):
          subset.append(nums[j])
      print(subset)
    """
    
    
      
      
    