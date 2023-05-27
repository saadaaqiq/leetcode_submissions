# https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    arr = [0]
    for n in nums:
      arr += [n^x for x in arr]
    return sum(arr)
    
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
    
    
      
      
    