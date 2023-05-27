# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
      if not nums: return 0
      
      parent = {}
      
      def find(x):
        if x != parent[x]: 
          parent[x] = find(parent[x])
        return parent[x]

      def union(x,y):
        parent[x] = x if x not in parent else parent[x]
        parent[y] = y if y not in parent else parent[y]
        parent[find(x)] = find(y)

      myset = set(nums)

      for n in nums:
        union(n,n)
        if n+1 in myset:
          union(n+1,n)
        
      c = Counter()
      for n in myset:
        c[find(n)] +=1

      return max(c.values())

            
            
            
            
            