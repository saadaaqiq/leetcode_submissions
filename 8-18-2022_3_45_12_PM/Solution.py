# https://leetcode.com/problems/sentence-similarity

class Solution:
  def areSentencesSimilar(self, s1, s2, sP):
    if len(s1) != len(s2):
      return False
    myset = set([tuple(tup) for tup in sP])
    for i in range(len(s1)):
      if s1[i] != s2[i] and (s1[i],s2[i]) not in myset and (s2[i],s1[i]) not in myset:
        return False
    return True