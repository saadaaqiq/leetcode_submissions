# https://leetcode.com/problems/word-break

class TreeNode():
  def __init__(self, value):
    self.val = value
    self.next = {}
  
class Solution:
  
  def wordBreak(self, text: str, wordList: List[str]) -> bool:
    
    tree = TreeNode(text)
    visited = { '' : True }
    
    def dfs(node):
      if node.val in visited:
        return visited[node.val]
      for word in wordList:
        if word in node.val:
          if word not in node.next:
            node.next[word] = []
          splitted = node.val.split(word)
          for part in splitted:
            nodePart = TreeNode(part)
            node.next[word].append(nodePart)
          res = True
          for partNode in node.next[word]:
            visited[partNode.val] = dfs(partNode)
            res = res and visited[partNode.val]
          if res:
            return True
          
      return False
    
    return dfs(tree)
    
    
            
          