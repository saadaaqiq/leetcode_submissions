# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution:
  def maxLength(self, arr: List[str]) -> int:
    
    def stob(s):
      b = 0
      for c in s:
        if b & (1<<(ord(c)-97)) != 0:
          return 0
        b = b | (1<<(ord(c)-97))
      return b
    
    def aorb(a, b):
      if stob(a) & stob(b) != 0:
        return 0
      return stob(a) | stob(b)
    
    def countones(mask):
      return Counter(bin(mask))["1"]
    
    dic = {i:[] for i in range(len(arr))}
    
    def dfs(i, mask):
      if i == len(arr):
        return countones(mask)
      b = stob(arr[i])
      if b & mask != 0:
        return dfs(i+1, mask)
      return max(dfs(i+1, b|mask), dfs(i+1, mask))
      
    return dfs(0, 0)
    
    
    
    
    
    
    
    
    
    
    