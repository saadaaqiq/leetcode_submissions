# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    visited = {}
    vis = set()
    parents = [i for i in range(len(nums))]
    
    def union(j):
      if nums[j] not in visited:
        visited[nums[j]] = j
        if nums[j]-1 in visited:
          i = visited[nums[j]-1]
          parents[j] = i
        if nums[j]+1 in visited:
          k = visited[nums[j]+1]
          parents[k] = j  
      
    for j in range(len(nums)):
      union(j)
    
    def find(i):
      c = 1
      j = i
      if j in vis:
        return c
      vis.add(j)
      while parents[j] != j:
        j = parents[j]
        if j not in vis:
          vis.add(j)
        c += 1
      return c
    
    m = 0
    for i in range(len(parents)):
      m = max(m, find(i))
      
    return m
      
    