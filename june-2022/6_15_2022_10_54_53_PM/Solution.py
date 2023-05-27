# https://leetcode.com/problems/shortest-word-distance-ii

class WordDistance:

  def __init__(self, wordsDict: List[str]):
    self.dic = { word : [] for word in wordsDict }
    for i, word in enumerate(wordsDict):
      self.dic[word].append(i)
    for word in self.dic:
      self.dic[word] = sorted(self.dic[word])
    
  def shortest(self, word1: str, word2: str) -> int:
    w1Locs = self.dic[word1]
    w2Locs = self.dic[word2]
    i, j = 0, 0
    mini = 30000
    while i < len(w1Locs) and j < len(w2Locs):
      mini = min(mini, abs(w1Locs[i]-w2Locs[j]))
      if w1Locs[i] < w2Locs[j]: 
        i += 1
      else:
        j += 1
    return mini
        
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)