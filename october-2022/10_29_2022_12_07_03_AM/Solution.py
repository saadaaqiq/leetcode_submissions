# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    i = 0
    myset = set()
    q = deque()
    res = 0
    while i < len(s):
      if s[i] in myset:
        myset.remove(s[i])
        c = q.popleft()
        while c != s[i]:
          if c in myset: myset.remove(c)
          c = q.popleft()
      myset.add(s[i])
      q.append(s[i])
      res = max(len(q), res)
      i += 1
    return res