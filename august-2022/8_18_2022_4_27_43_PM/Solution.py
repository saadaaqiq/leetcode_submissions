# https://leetcode.com/problems/sentence-similarity-ii

class Solution:
  
  def areSentencesSimilarTwo(self, s1, s2, sP):
    
    if len(s1) != len(s2):
      return False
    
    dic = {}
    for word, sim in sP:
      if word not in dic:
        dic[word] = set()
      if sim not in dic:
        dic[sim] = set()
      dic[word].add(sim)
      dic[sim].add(word)
      
    visited = set()
    
    def sim(a, b):
      if a in visited or a not in dic:
        return False
      if b in dic[a]:
        return True
      visited.add(a)
      for s in dic[a]:
        if sim(s, b):
          visited.remove(a)
          return True
      visited.remove(a)
      return False
      
    for i in range(len(s1)):
      if s1[i] != s2[i] and not sim(s1[i], s2[i]) and not sim(s2[i], s1[i]):
        return False

    return True