# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

class Solution:
  
  def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    dic = {}
    i,j = 0,0
    m = 0
    
    while j < len(s):
      if len(dic) < 2:
        if s[j] not in dic:
          dic[s[j]] = 0
        dic[s[j]] += 1
        j += 1
      else:
        if s[j] not in dic:
          dic.clear()
          dic[s[j]] = 0
          i = 0
          while i+j-1 >= 0 and s[i+j-1] == s[j-1]:
            i -= 1
          dic[s[j-1]] = -i
        dic[s[j]] += 1
        j += 1
      m = max(m, sum(list(dic.values())))
    
    return m