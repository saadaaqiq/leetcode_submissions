# https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                w = []
                while stack[-1] != "[":
                    w.append(stack.pop())
                txt = ''.join(list(reversed(w)))
                stack.pop()
                n = []
                while stack and stack[-1].isnumeric():
                    n.append(stack.pop())
                num = int(''.join(list(reversed(n))))
                stack.append(num * txt)
        return ''.join(stack)
                
            
            
            

            


