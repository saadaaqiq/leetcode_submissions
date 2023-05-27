# https://leetcode.com/problems/generalized-abbreviation

class Solution:
  def generateAbbreviations(self, word):
    
    def dfs(c, w):
      res = []
      if not w: return ["1", c]
      mylist = dfs(w[0], w[1:])
      for sub in mylist:
        
        res.append(c + sub)
        
        if (len(sub)==1 and sub[0].isnumeric()) or (len(sub) >= 2 and sub[0].isnumeric() and not sub[1].isnumeric()):
          res.append(str(1 + int(sub[0])) + sub[1:])
        elif len(sub) >= 2 and sub[0].isnumeric() and sub[1].isnumeric():
          res.append(str(1 + int(sub[0]+sub[1])) + sub[2:])
        elif not sub[0].isnumeric():
          res.append("1" + sub)
          
      return res
    
    return dfs(word[0], word[1:])