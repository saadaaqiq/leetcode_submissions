# https://leetcode.com/problems/find-permutation

class Solution:
  def findPermutation(self, s: str) -> List[int]:
    res = [ i+1 for i in range(0, len(s)+1) ]
    i = 0
    while i < len(s):
      if s[i] == "I":
        i += 1
        continue
      j = i
      while j < len(s) and s[j] == "D":
        j += 1
      temp = res[j]
      for k in range(i, j+1):
        res[k] = temp - k + i        
      i = j
    return res