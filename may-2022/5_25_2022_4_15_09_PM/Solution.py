# https://leetcode.com/problems/word-search-ii

class Trie:
  
  def __init__(self):
    self.val = None
    self.ok = False
    self.next = {}
    
  def insert(self, word):
    node = self
    for char in word:
      letter = Trie()
      if char in node.next:
        letter = node.next[char]
      else:
        letter = Trie()
        letter.val = char
      node.next[char] = letter
      node = letter

  def startsWith(self, word):
    node = self
    for i, char in enumerate(word):
      if not char in node.next:
        return False
      else:
        node = node.next[char]
        if not node.ok:
          return False
        else:
          if i == len(word) - 1:
            return True

class Solution:
  
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
    rows, columns = len(board), len(board[0])
    root = Trie()
    for word in words:
      root.insert(word)
    visited = set()
    
    def isInBoard(i,j,node):
      visited.add((i,j))
      if not node.ok:
        node.ok = True
      if i>0 and board[i-1][j] in node.next and (i-1,j) not in visited:
        isInBoard(i-1, j, node.next[board[i-1][j]])
      if i<rows-1 and board[i+1][j] in node.next and (i+1,j) not in visited:
        isInBoard(i+1, j, node.next[board[i+1][j]])
      if j>0 and board[i][j-1] in node.next and (i,j-1) not in visited:
        isInBoard(i, j-1, node.next[board[i][j-1]])
      if j<columns-1 and board[i][j+1] in node.next and (i,j+1) not in visited:
        isInBoard(i, j+1, node.next[board[i][j+1]])
      visited.remove((i,j))
                
    for i in range(rows):
      for j in range(columns):
        if board[i][j] in root.next:
          isInBoard(i,j,root.next[board[i][j]])
    result = []
    for word in words:
      if root.startsWith(word):
        result.append(word)
      
    return result
        
        
        
        
        
        
        
        
        
    