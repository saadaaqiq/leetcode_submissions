# https://leetcode.com/problems/valid-word-square

class Solution:
  def validWordSquare(self, words: List[str]) -> bool:
    n = len(words)
    m = max([len(word) for word in words])
    if n != m:
      return False
    complement = [ "."*(m-len(word))  for word in words ]
    for i in range(n):
      for j in range(n):
        if (words[i]+complement[i])[j] != (words[j]+complement[j])[i]:
          return False
    return True
