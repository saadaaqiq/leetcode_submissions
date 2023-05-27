# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter

class Solution:
  def countLetters(self, s: str) -> int:
    n, res, old, i, j = len(s), 0, s[0], 0, 0
    while j < n:
      while i < n and s[i] == old:
        i += 1
      res += (i-j) * (i-j+1) // 2
      j = i
      old = s[i] if i < n else old
    return res   