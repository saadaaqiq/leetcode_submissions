# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums: return 0  
    parent, rank = {}, {}
    for n in nums: parent[n], rank[n] = n, 0
    
    def find(n):
      if parent[n] != n: parent[n] = find(parent[n])
      return parent[n]
    
    def union(n,m):
      p, q = find(n), find(m)
      if rank[p] > rank[q]: parent[q] = p
      elif rank[p] < rank[q]: parent[p] = q
      else: parent[q], rank[p] = p, rank[p] + 1
    
    for n in nums:
      if n+1 in parent: union(n, n+1)
        
    for n in parent: find(n)
      
    return max(Counter(parent.values()).values())
    
    
          