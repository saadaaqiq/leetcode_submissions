# https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:
  
  def __init__(self):
    self.val = None
    self.next = { chr(k+97) : None for k in range(26) }
    
  def insert(self, word: str) -> None:
    old = self
    for c in word:
      letter = Trie()
      if old.next[c]:
        letter = old.next[c]
      else:
        letter = Trie()
        letter.val = c
      old.next[c] = letter
      old = letter
    old.next['end'] = True
      
  def emptyDic(self, dic):
    isEmpty = True
    for k in dic:
      if dic[k]:
        isEmpty = False
    return isEmpty
  
  def search(self, word: str) -> bool:
    old = self
    if self.emptyDic(old.next):
      return False
    for i in range(len(word)):
      if not old.next[word[i]]:
        return False
      else:
        old = old.next[word[i]]
        if i == len(word) - 1:
          return 'end' in old.next
          
  def startsWith(self, prefix: str) -> bool:
    old = self
    if self.emptyDic(old.next):
      return False
    for i in range(len(prefix)):
      if not old.next[prefix[i]]:
        return False
      else:
        old = old.next[prefix[i]]
    return True
      
