# https://leetcode.com/problems/generalized-abbreviation

class Solution:
  def generateAbbreviations(self, word):
    
    def dfs(c, w):
      res = []
      if not w:
        return ["1", c]
      mylist = dfs(w[0], w[1:])
      for sub in mylist:
        res.append(c + sub)
        res.append("1" + sub)
      return res
    
    res = dfs(word[0], word[1:])
    
    newres = []
    
    for w in res:
      new = ""
      f = 0
      for c in w:
        if c!="1":
          if f!=0:
            new += str(f)
            f = 0
          new += c
        else:
          f += 1
      if f!=0: 
        new += str(f)
      newres.append(new)
    
    return newres
          