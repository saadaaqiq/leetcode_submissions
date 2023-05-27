# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    dic = {}
    i, j = 0, 0
    m = 0
    while j < len(s):
      if s[j] not in dic: 
        dic[s[j]] = 0
      dic[s[j]] += 1
      while dic[s[j]] > 1:
        dic[s[i]] -= 1
        i += 1
      m = max(m, sum(dic.values()))
      j += 1
    return m