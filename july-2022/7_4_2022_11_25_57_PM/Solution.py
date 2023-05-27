# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
  
  def evalRPN(self, tokens: List[str]) -> int:
    
    ops = ["+", "-", "/", "*"]
    
    def operate(a,b,op):
      if op == ops[0]:
        return a+b
      elif op == ops[1]:
        return a-b
      elif op == ops[2]:
        return int(a/b)
      elif op == ops[3]:
        return a*b
      else:
        return 1
    
    stack = []
    for i, token in enumerate(tokens):
      if token not in ops:
        stack.append(token)
      else:
        b,a = stack.pop(), stack.pop()
        stack.append(operate(int(a),int(b),token))
    
    return stack[-1]