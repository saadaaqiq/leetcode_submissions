# https://leetcode.com/problems/generate-parentheses

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    res = []
    stack = []
    
    def gen(op,cl):
      if op == n and cl == n:
        res.append("".join(stack))
        return
      elif op == n and cl < op:
        stack.append(')')
        gen(op, cl+1)
        stack.pop()
      elif op < n and cl == op:
        stack.append('(')
        gen(op+1, cl)
        stack.pop()
      elif op < n and cl < op:
        stack.append('(')
        gen(op+1, cl)
        stack.pop()
        stack.append(')')
        gen(op, cl+1)
        stack.pop()
      else:
        return
      
    gen(0,0)
    return res
    
      
    
    
      