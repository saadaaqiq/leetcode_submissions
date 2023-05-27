# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    j = 0
    myset = set()
    res = 0
    for i in range(len(s)):
      while s[i] in myset:
        myset.remove(s[j])
        j += 1
      myset.add(s[i])
      res = max(len(myset), res)
    return res
