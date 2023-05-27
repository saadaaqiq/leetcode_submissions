# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    TOTAL = len(numSet)
    visited = set()
    m = 0
    
    for num in numSet:
      if num not in visited:
        visited.add(num)
        seq = []
        if num-1 not in numSet:
          seq.append(num)
          c=1
          while num+c in numSet:
            visited.add(num+c)
            seq.append(num+c)
            c+=1
          m = max(m,c)
        if len(visited)==TOTAL:
          break
    
    return m
        
    