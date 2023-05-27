# https://leetcode.com/problems/generate-parentheses

class Solution:
  
  def generateParenthesis(self, num: int) -> List[str]:
    
    dic = { i: set() for i in range(1, num+1) }
    
    def gen(n):
      if dic[n]:
        return dic[n]
      if n == 1:
        dic[n].add('()')
      else:
        if not dic[n-1]:
          dic[n-1] = gen(n-1)
        for s in dic[n-1]:
          dic[n].add('(' + s + ')')
        for i in range(1,n):
          if not dic[i]:
            dic[i] = gen(i)
          if not dic[n-i]:
            dic[n-i] = gen(n-i)
          for s1 in dic[i]:
            for s2 in dic[n-i]:
              dic[n].add(s1 + s2)
      return dic[n]
    
    return gen(num)
