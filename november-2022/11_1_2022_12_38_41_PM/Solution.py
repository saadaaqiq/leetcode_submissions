# https://leetcode.com/problems/decode-ways

class Solution:
  def numDecodings(self, text: str) -> int:
    cache = {}
    
    def dfs(s):
      if not s or (len(s)==1 and s!="0"): return 1
      if s[0] == '0': return 0
      if s in cache: return cache[s]
      if int(s[:2]) <= 26:
        if s[:2][1] == '0':
          cache[s[2:]] = dfs(s[2:]) if s[2:] not in cache else cache[s[2:]]
          return cache[s[2:]]
        else:
          cache[s[2:]] = dfs(s[2:]) if s[2:] not in cache else cache[s[2:]]
          cache[s[1:]] = dfs(s[1:]) if s[1:] not in cache else cache[s[1:]]
          return cache[s[1:]] + cache[s[2:]]
      else:
        if s[:2][1] == '0': 
          return 0
        else:
          if s[1:] not in cache:
            cache[s[1:]] = dfs(s[1:])
          return cache[s[1:]]
    
    return dfs(text)