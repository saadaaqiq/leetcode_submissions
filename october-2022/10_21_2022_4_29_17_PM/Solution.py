# https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    arr = [0]
    for num in nums:
      arr += [num^arr[i] for i in range(len(arr)-1,-1,-1)]
    return sum(arr)

    
    
      
      
    