# https://leetcode.com/problems/group-shifted-strings

class Solution:
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    dic = {}
    
    def getNextString(s):
      return ''.join([chr((ord(c)%97 + 1)%26+97) for c in s])
    
    def genPossibilities(s):
      res = [ s ]
      for i in range(25):
        res.append(getNextString(res[-1]))
      res.sort()
      return tuple(res)
    
    for s in strings:
      poss = genPossibilities(s)
      if poss not in dic:
        dic[poss] = []
      dic[poss].append(s)
    
    return list(dic.values())
