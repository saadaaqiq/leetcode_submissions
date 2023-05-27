# https://leetcode.com/problems/word-pattern-ii

class Solution:
  def wordPatternMatch(self, pattern: str, s: str) -> bool:
    n, m = len(s), len(pattern)
    W, P = {}, {}

    def dfs(i, k):
      nonlocal n, m
      if k == m or i == n: return k == m and i == n
      c, added = pattern[k], False
      for j in range(i, n):
        sub = s[i:j+1]
        if (c in P and P[c]!=sub) or (sub in W and W[sub]!=c):  continue
        if c not in P and sub not in W: P[c], W[sub], added = sub, c, True
        if dfs(j+1, k+1): return True
        if added:
          del W[sub]
          del P[c]
      return False

    return dfs(0, 0)


    