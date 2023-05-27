# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters

class Solution:
  
  def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
    
    if k > len(s) or k > 26: return 0
    
    res = 0
    freq = [0 for i in range(26)]
    for i in range(k):
      freq[ord(s[i])-97] += 1
    
    def checkem():
      if sum(freq) != k:
        return False
      for i in freq:
        if i > 1:
          return False
      return True
    
    l, r = 0, k-1
    while r < len(s)-1:
      if checkem():
        res += 1
      freq[ord(s[l])-97] -= 1
      l+=1
      r+=1
      freq[ord(s[r])-97] += 1
    if checkem():
        res += 1
        
    return res
  
