# https://leetcode.com/problems/isomorphic-strings

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    s_t = {}
    t_s = {}
    for i in range(len(s)):
      if s[i] not in s_t:
        s_t[s[i]] = set()
      s_t[s[i]].add(t[i])
      if t[i] not in t_s:
        t_s[t[i]] = set()
      t_s[t[i]].add(s[i])
    for k in s_t:
      if len(s_t[k]) > 1:
        return False
    for k in t_s:
      if len(t_s[k]) > 1:
        return False
    return True