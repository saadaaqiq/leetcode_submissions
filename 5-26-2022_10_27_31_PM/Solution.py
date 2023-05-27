# https://leetcode.com/problems/longest-common-subsequence

class Solution:
  def longestCommonSubsequence(self, s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    grid = [[ 0 for j in range(n+1) ] for i in range(m+1)]
    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        if s1[i]==s2[j]:
          grid[i][j] = 1 + grid[i+1][j+1]
        else:
          grid[i][j] = max(grid[i+1][j], grid[i][j+1])
    print(grid)
    return grid[0][0]