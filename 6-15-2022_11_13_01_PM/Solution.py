# https://leetcode.com/problems/shortest-word-distance-iii

class Solution:
  def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    
    dic, mySet = collections.defaultdict(list), set([word1,word2])
    
    for i, word in enumerate(wordsDict):
      if word in mySet:
        dic[word].append(i)
    
    for word in mySet:
      dic[word] = sorted(dic[word])
        
    if len(dic) == 1:
      return min([dic[word1][i+1] - dic[word1][i] for i in range(len(dic[word1])-1)])
    else:
      a, b, mini = 0, 0, sys.maxsize
      while a < len(dic[word1]) and b < len(dic[word2]):
        mini = min(mini, abs(dic[word1][a] - dic[word2][b]))
        if dic[word1][a] > dic[word2][b]:
          b+=1
        else:
          a+=1
      return mini