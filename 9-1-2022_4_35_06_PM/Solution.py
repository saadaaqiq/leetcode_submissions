# https://leetcode.com/problems/find-permutation

class Solution:
  def findPermutation(self, s: str) -> List[int]:
    res = [i+1 for i in range(0, len(s)+1)]
    dic = {} 
    for i in range(len(s)-1, -1, -1):
      if s[i] == "D":
        dic[i] = 1
        if i<len(s)-1 and i+1 in dic:
          dic[i] += dic[i+1]
          del dic[i+1]
    for k in dic:
      for i in range(k,k+dic[k]+1):
        res[i] = k+dic[k]+1 - i + k
    return res
      
        
        
    
        