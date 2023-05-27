# https://leetcode.com/problems/split-array-into-consecutive-subsequences

class Solution:
  
  def isPossible(self, nums: List[int]) -> bool:
    
    dic = {}
    
    for num in nums:

      if num-1 not in dic:
        if num in dic:
          heapq.heappush(dic[num], 1)
        else:
          dic[num] = [1]
          heapq.heapify(dic[num])
          
      else:
        m = heapq.heappop(dic[num-1])
        if len(dic[num-1]) == 0:
          dic.pop(num-1)
        if num in dic:
          heapq.heappush(dic[num], m+1)
        else:
          dic[num] = [m+1]
          heapq.heapify(dic[num])
        
    for k in dic:
      for f in dic[k]:
        if f < 3:
          return False
    
    return True
    
      
  
  
  
  
  