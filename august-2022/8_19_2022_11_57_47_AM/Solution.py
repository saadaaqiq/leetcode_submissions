# https://leetcode.com/problems/valid-word-square

class Solution:
  def validWordSquare(self, words: List[str]) -> bool:
    
    n = max([len(word) for word in words])
    m = max(n, len(words))
    grid = [['' for j in range(m)] for i in range(m)]
    for i, word in enumerate(words):
      for j in range(len(word)):
        grid[i][j] = word[j]
        
    for i in range(m):
      for j in range(m):
        if grid[i][j] != grid[j][i]:
          return False
        
    return True
