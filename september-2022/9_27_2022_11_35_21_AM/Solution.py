# https://leetcode.com/problems/satisfiability-of-equality-equations

class Solution:
  
  def equationsPossible(self, equations: List[str]) -> bool:
    
    equals = [set([i]) for i in range(26)]
    different = set()
    
    for string in equations:
      if string[1] == '=':
        equals[ord(string[0])-97].add(ord(string[3])-97)
        equals[ord(string[3])-97].add(ord(string[0])-97)
      else:
        different.add((ord(string[0])-97, ord(string[3])-97))
    
    for i in range(26):
      for j in range(26):
        if j in equals[i] or i in equals[j]:
          equals[i] = equals[i].union(equals[j])
          
    def inSameSet(x,y,methSet):
      for s in methSet:
        if x in s and y in s:
          return True
      return False
    
    for x, y in different:
      if inSameSet(x, y, equals):
        return False
    
    return True