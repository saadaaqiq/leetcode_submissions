# https://leetcode.com/problems/decode-ways

class Solution:
  def numDecodings(self, text: str) -> int:
    visited = {}
    
    def dfs(s):
      if len(s) == 0 or (len(s) == 1 and s[0] != '0'):
        return 1
      if s[0] == '0':
        return 0
      if s in visited:
        return visited[s]
      
      if int(s[:2]) <= 26:
        if s[:2][1] == '0':
          visited[s[2:]] = dfs(s[2:])
          return visited[s[2:]]
        else:
          visited[s[2:]], visited[s[1:]] = dfs(s[2:]), dfs(s[1:])
          return visited[s[2:]] + visited[s[1:]]
      else:
        visited[s[1:]] = dfs(s[1:])
        return visited[s[1:]] if s[:2][1] != '0' else 0
    
    return dfs(text)