# https://leetcode.com/problems/valid-word-square

class Solution:
  def validWordSquare(self, words: List[str]) -> bool:
    n = len(words)
    if n != max([len(word) for word in words]):
      return False
    grid = [['' for j in range(n)] for i in range(n)]
    for i, word in enumerate(words):
      for j in range(len(word)):
        grid[i][j] = word[j]
    for i in range(n):
      for j in range(n):
        if grid[i][j] != grid[j][i]:
          return False
        
    return True
