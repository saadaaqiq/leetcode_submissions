# https://leetcode.com/problems/design-add-and-search-words-data-structure

class WordDictionary:

  def __init__(self):
    self.val = None
    self.next = {  }
    
  

  def addWord(self, word: str) -> None:
    old = self
    for c in word:
      if c in old.next:
        letter = old.next[c]
      else:
        letter = WordDictionary()
        letter.val = c
        old.next[c] = letter
      old = letter
    old.next['end'] = True

  def search(self, word: str) -> bool:
    old = self
    if not old.next:
      return False
    if len(word) == 0 and 'end' in old.next:
      return True
    for i,c in enumerate(word):
      if c != '.':
        if c not in old.next:
          return False
        else:
          old = old.next[c]
          if i == len(word) - 1:
            return 'end' in old.next
      else:         
        for k in old.next:
          if k!='end' and old.next[k].search(word[i+1:]):
            return True
        return False
                             