# https://leetcode.com/problems/word-ladder

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    dic = {}
    for word in (wordList + [beginWord]):
      for i in range(len(beginWord)):
        w = word[:i] + '*' + word[i+1:]
        if w not in dic:
          dic[w] = []
        dic[w].append(word)
    adj = {}
    for k in dic:
      for i in range(len(dic[k])):
        for j in range(len(dic[k])):
          if i!=j:
            if dic[k][i] not in adj:
              adj[dic[k][i]] = []
            adj[dic[k][i]].append(dic[k][j])
    q = deque()
    q.append((beginWord,1))
    visited = set()
    while q:
      word,l = q.popleft()
      visited.add(word)
      if word == endWord:
        return l
      for w in adj[word]:
        if w not in visited:
          q.append((w,l+1))
    return 0
      