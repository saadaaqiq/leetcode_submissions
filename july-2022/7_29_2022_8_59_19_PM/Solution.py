# https://leetcode.com/problems/word-ladder

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    if endWord not in wordList:
      return 0
    q = deque([(beginWord, 1)])
    s = 'abcdefghijklmnopqrstuvwxyz'
    while q:
      w,l = q.popleft()
      for i, c in enumerate(w):
        for letter in s:
          new = w[:i] + letter + w[i+1:]
          if new == endWord:
            return l + 1
          if new in wordList:
            wordList.discard(new)
            q.append((new,l+1))
    return 0
