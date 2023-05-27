# https://leetcode.com/problems/shortest-word-distance-iii

class Solution:
  def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    dic = collections.defaultdict(list)
    for i, word in enumerate(wordsDict):
      if word == word1 or word == word2:
        dic[word].append(i)
    if len(dic) == 1:
      arr = sorted(dic[word1])
      mini = 1000000
      i = 0
      while i < len(arr)-1:
        mini = min(mini, arr[i+1]-arr[i])
        i+=1
      return mini
    else:
      A = sorted(dic[word1])
      B = sorted(dic[word2])
      mini = 1000000
      a,b = 0,0
      while a < len(A) and b < len(B):
        mini = min(mini, abs(A[a] - B[b]))
        if A[a] > B[b]:
          b+=1
        else:
          a+=1
      return mini