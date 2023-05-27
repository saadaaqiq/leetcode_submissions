# https://leetcode.com/problems/add-bold-tag-in-string

class Solution:
  def addBoldTag(self, s: str, words: List[str]) -> str:
    n, close, res = len(s), -1, ""
    for i in range(n):
      for w in words:
        if i + len(w) <= len(s) and s[i:i+len(w)]==w:
          if close < i:
            res += "<b>"
          close = max(close, i + len(w))
      if close == i:
        res += "</b>"
      res += s[i]
    if close == len(s):
      res += "</b>"
    return res