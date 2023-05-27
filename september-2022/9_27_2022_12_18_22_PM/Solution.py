# https://leetcode.com/problems/satisfiability-of-equality-equations

class Solution:
  
  def equationsPossible(self, equations: List[str]) -> bool:
    
    equals = [set([i]) for i in range(26)]
    differents = [set() for i in range(26)]
    
    for string in equations:
      if string[1] == '=':
        equals[ord(string[0])-97].add(ord(string[3])-97)
        equals[ord(string[3])-97].add(ord(string[0])-97)
      else:
        differents[ord(string[0])-97].add(ord(string[3])-97)
        differents[ord(string[3])-97].add(ord(string[0])-97)
    
    for eqSet in equals:
      for k in eqSet:
        equals[k] = equals[k].union(eqSet)
    
    for i in range(26):
      if len(equals[i].intersection(differents[i]))>0:
        return False
      
    return True
      
    
    
    
    