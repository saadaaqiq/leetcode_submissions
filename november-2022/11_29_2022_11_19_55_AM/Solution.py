# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    if k==0:
      return 0
    n = len(s)
    dic = {}
    i, j = 0, 0
    res = 0
    while j < n:
      if s[j] in dic or len(dic) < k:
        if s[j] not in dic:
          dic[s[j]] = 0
        dic[s[j]] += 1
        res = max(res, j-i+1)
        j += 1
      else:
        dic[s[i]] -= 1
        if dic[s[i]] == 0: 
          dic.pop(s[i])
        i += 1
    return res