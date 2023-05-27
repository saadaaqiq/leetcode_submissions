# https://leetcode.com/problems/generate-parentheses

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    res = []
    
    def gen(s,op,cl):
      if op == n and cl < n:
        res.append(s + ')'*(n-cl))
        return
      if op > cl:
        gen(s + ')', op, cl+1)
      gen(s + '(', op+1, cl)

    gen('',0,0)
    return res
    
      
    
    
      