# https://leetcode.com/problems/unique-paths

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    if m == 1 or n == 1:
      return 1
    current, prev = [0 if i < m-1 else 1 for i in range(m)], [1 for i in range(m)]

    for j in range(n-2, -1, -1):
      for i in range(m-2, -1, -1):
        current[i] = prev[i] + current[i+1]
      prev = current
    return current[0]