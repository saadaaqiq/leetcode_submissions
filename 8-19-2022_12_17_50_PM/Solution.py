# https://leetcode.com/problems/valid-word-square

class Solution:
  def validWordSquare(self, words: List[str]) -> bool:
    n = len(words)
    for i, word in enumerate(words):
      if ''.join([word[i] for word in words if i < len(word)])!= word:
        return False
    return True