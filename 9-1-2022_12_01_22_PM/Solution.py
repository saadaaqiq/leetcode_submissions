# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter

class Solution:
  def countLetters(self, s: str) -> int:
    res, i, j = 0, 0, 0
    while j < len(s):
      while i < len(s) and s[i] == s[j]:
        i += 1
      res += (i-j) * (i-j+1) // 2
      j = i
    return res   